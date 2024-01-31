import torch
from fastdup.sentry import fastdup_capture_exception
from fastdup.definitions import MISSING_LABEL
from tqdm import tqdm
import nltk
nltk.download('stopwords')
device_to_captioner = {}
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


# pip install setuptools -U
# pip install git+https://github.com/xinyu1205/recognize-anything.git
# wget https://huggingface.co/spaces/xinyu1205/recognize-anything/resolve/main/ram_swin_large_14m.pth
import logging
import os
import wget
import torch
import numpy as np
import polars as pl
from PIL import Image
from argparse import ArgumentParser
from torch.utils.data import DataLoader, Dataset
from typing import List, Union, Iterable, Any, Tuple, Optional
import traceback
from threading import Thread
from typing import Callable, Any, Iterable, Dict

try:
    from ram.models import ram
    from ram.models.ram import RAM
    from ram import get_transform
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        'failed to import ram, download ram by running the following commands:\n'
        'pip install setuptools -U\n'
        'pip install git+https://github.com/xinyu1205/recognize-anything.git'
    )

TRANSFORM = get_transform(image_size=384)
ram_model = None

class ReturnValueThread(Thread):
    def __init__(self, target: callable, name: str = None, args: Iterable[Any] = (),
                 kwargs: Dict[str, Any] = None, daemon: bool = None) -> None:
        super().__init__(target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)

    def run(self) -> None:
        self._value = self._target(*self._args, **self._kwargs)

    def return_value(self) -> Any:
        return self._value

# Use a class with __getitem__ to make sure that not all images are loaded into memory at once.
class ImageDataset(Dataset):
    def __init__(self, filenames: List[str], transform: callable):
        self.filenames = filenames
        self.transform = transform

    def __len__(self) -> int:
        return len(self.filenames)

    def __getitem__(self, index: int) -> torch.Tensor:
        return self.transform(Image.open(self.filenames[index]))


def tag(ram: RAM, image: torch.Tensor) -> Tuple[List[str], List[str], torch.Tensor]:
    label_embed = torch.nn.functional.relu(ram.wordvec_proj(ram.label_embed))

    image_embeds = ram.image_proj(ram.visual_encoder(image))
    image_atts = torch.ones(image_embeds.size()[:-1],
                            dtype=torch.long).to(image.device)

    # recognized image tags using image-tag recogntiion decoder
    image_cls_embeds = image_embeds[:, 0, :]
    image_spatial_embeds = image_embeds[:, 1:, :]

    bs = image_spatial_embeds.shape[0]
    label_embed = label_embed.unsqueeze(0).repeat(bs, 1, 1)
    tagging_embed = ram.tagging_head(
        encoder_embeds=label_embed,
        encoder_hidden_states=image_embeds,
        encoder_attention_mask=image_atts,
        return_dict=False,
        mode='tagging',
    )

    logits = ram.fc(tagging_embed[0]).squeeze(-1)

    targets = torch.where(
        torch.sigmoid(logits) > ram.class_threshold.to(image.device),
        torch.tensor(1.0).to(image.device),
        torch.zeros(ram.num_class).to(image.device))

    tag = targets.cpu().numpy()
    tag[:, ram.delete_tag_index] = 0
    tag_output = []
    tag_output_chinese = []
    for b in range(bs):
        index = np.argwhere(tag[b] == 1)
        token = ram.tag_list[index].squeeze(axis=1)
        tag_output.append(' | '.join(token))
        token_chinese = ram.tag_list_chinese[index].squeeze(axis=1)
        tag_output_chinese.append(' | '.join(token_chinese))

    return tag_output, tag_output_chinese, logits


# Function for generating tags on a given dataset
def run_batch_inference(image_list: List[str],
                        batch_size: int, device: int) -> pl.DataFrame:
    def _preprocess(data_iterator: Iterable, device: int) -> Any:
        with torch.device(device):
            batch_images = next(data_iterator)
            batch_images = batch_images.to(device, torch.float16 if device != 'cpu' else torch.float32)

        return batch_images

    dataset = ImageDataset(image_list, TRANSFORM)
    dataloader = DataLoader(dataset, batch_size=batch_size, num_workers=2)

    all_tags = []
    data_iterator = iter(dataloader)

    if len(image_list) > 0:
        try:
            batch_images = _preprocess(data_iterator, device)
        except Exception as e:
            logging.exception(f'failed to process batch 0-{batch_size}: {e}')

    for i in range(len(dataloader)):
        try:
            has_next_batch = (i + 1) < len(dataloader)

            if has_next_batch:
                thread = ReturnValueThread(target=_preprocess, args=(data_iterator, device))
                thread.start()

            with torch.inference_mode():
                english_tags, chinese_tags, logits = tag(ram_model, batch_images)

            tags = [tag.split(" | ") for tag in english_tags]
            all_tags.extend(tags)  # [0] - English tags, [1] - Chinese tags

            if has_next_batch:
                thread.join()
                batch_images = thread.return_value()
        except Exception as e:
            all_tags.extend([None] * batch_size)
            logging.exception(f'failed to tag batch {i}: {e}')

    # Add results to the DataFrame
    #tags_series = pl.Series("tags", all_tags, dtype=pl.List(pl.Utf8))
    output_df = list(all_tags)

    if device != 'cpu':
        torch.cuda.empty_cache()

    return output_df


def verify_ram_model(model_path: str, download_model: bool) -> None:
    if os.path.exists(model_path):
        return

    if download_model:
        model_url = 'https://huggingface.co/spaces/xinyu1205/recognize-anything/resolve/main/ram_swin_large_14m.pth'
        wget.download(model_url, model_path)
        assert os.path.exists(model_path), 'failed to download model'
        return

    assert os.path.exists(model_path), f'failed to find model at {model_path}'

def init_ram_tag_job(batch_size: int = 64,
        model_path: str = 'ram_swin_large_14m.pth',
        device = 0,
        verbose: bool = True) -> dict:

    global ram_model
    verify_ram_model(model_path, True)
    with torch.device(device):
        model = ram(pretrained=model_path, image_size=384, vit='swin_l')
        model.eval()
        model = model.to(device, torch.float16 if device != "cpu" else torch.float32)


    ram_model = model

def format_captions(captions):

    # Remove stop words
    filtered_text = ' '.join(word for word in captions.split()[:8] if word.lower() not in stop_words)
    # Split the text into words and count their occurrences
    return filtered_text

def init_captioning(model_name='automatic', device='cpu', batch_size=8, max_new_tokens=20,
                        use_float_16=True):

    global device_to_captioner
    # use GPU if device is specified
    if isinstance(device, str):
        if device == 'gpu':
            device = 0
        elif device == 'cpu':
            use_float_16 = False

    # confirm necessary dependencies are installed, and import them
    try:
        from transformers import pipeline
        from transformers.utils import logging
        logging.set_verbosity(50)



    except Exception as e:
        fastdup_capture_exception("Auto generate labels", e)
        print("Auto captioning requires an installation of the following libraries:\n")
        print("   huggingface transformers\n   pytorch\n")
        print("   to install, use `pip3 install transformers torch`")
        raise


    model = "Salesforce/blip-image-captioning-large"
    has_gpu = torch.cuda.is_available()
    captioner = pipeline("image-to-text", model=model, device=device if has_gpu else "cpu", max_new_tokens=max_new_tokens,
                         torch_dtype=torch.float16 if use_float_16 else torch.float32)
    device_to_captioner[device] = captioner

    try:
        init_ram_tag_job(device=device, verbose=True)
    except Exception as e:
      print("Failed to init ram job", traceback.format_exc())

    return captioner

def generate_labels(filenames, model_name='automatic', device = 'cpu', batch_size=8, max_new_tokens=20, use_float_16=True):
    global device_to_captioner
    if device not in device_to_captioner:
        captioner = init_captioning(model_name, device, batch_size, max_new_tokens, use_float_16)
    else:
        captioner = device_to_captioner[device]



    captions = []
    # generate captions
    # try:
    #     for i in tqdm(range(0, len(filenames), batch_size)):
    #         chunk = filenames[i:i + batch_size]
    #         try:
    #             for pred in captioner(chunk, batch_size=batch_size):
    #                 charstring = ' '
    #                 caption = charstring.join([d['generated_text'] for d in pred])
    #                 # Split the sentence into words
    #                 words = caption.split()
    #                 # Filter out words containing '#'
    #                 filtered_words = [word for word in words if '#' not in word]
    #                 # Join the filtered words back into a sentence
    #                 caption = ' '.join(filtered_words)
    #                 caption = caption.strip()
    #                 caption = format_captions(caption)
    #                 captions.append(caption)
    #         except Exception as ex:
    #             print("Failed to caption chunk", chunk[:5], ex)
    #             captions.extend([MISSING_LABEL] * len(chunk))
    #
    # except Exception as e:
    #     fastdup_capture_exception("Auto caption image", e)
    #     return [MISSING_LABEL] * len(filenames)

    print('runing batch ')
    captions.extend(run_batch_inference(filenames, batch_size=10, device=device))

    return captions

if __name__ == "__main__":
    import fastdup
    #from fastdup.fast_captions import generate_labels
    file = "/Users/dannybickson/visual_database/cxx/unittests/two_images/"
    import os
    files = os.listdir(file)
    files = [os.path.join(file, f) for f in files]
    ret = generate_labels(files, model_name='blip')
    assert(len(ret) == 2)
    print(ret)
    for r in ret:
        assert "shelf" in r or "shelves" in r or "various" in r
