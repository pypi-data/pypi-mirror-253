import os
import gdown
from pathlib import Path
from typing import Optional, Union

CRAFT_GDRIVE_URL = "https://drive.google.com/uc?id=1bupFXqT-VU6Jjeul13XP7yx2Sg5IHr4J"
PARSEQ_GDRIVE_URL = "https://drive.google.com/uc?id=1xcE9qpJXp4ofINwXWVhhQIh9S8Z7cuGj"

def download(url: str, save_path: str):
    """
    Downloads file from gdrive, shows progress.
    Example inputs:
        url: 'ftp://smartengines.com/midv-500/dataset/01_alb_id.zip'
        save_path: 'data/file.zip'
    """

    # create save_dir if not present
    create_dir(os.path.dirname(save_path))
    # download file
    gdown.download(url, save_path, quiet=False)


def create_dir(_dir):
    """
    Creates given directory if it is not present.
    """
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def ocr_model_download(weight_path = None,model="recognize"):

    if model == "recognize":
        file_name_model = "parseq_tamil_v6.ckpt"
        url = CRAFT_GDRIVE_URL
    else:
        file_name_model = "craft_mlt_25k.pth"
        url = PARSEQ_GDRIVE_URL

    # get craft net path
    if weight_path is None:
        home_path = str(Path.home())
        weight_path = Path(
            home_path,
            ".tamil_ocr",
            "weights",
            file_name_model
        )
    weight_path = Path(weight_path).resolve()
    weight_path.parent.mkdir(exist_ok=True, parents=True)
    weight_path = str(weight_path)

    # check if weights are already downloaded, if not download
    
    if not os.path.isfile(weight_path):
        print("Craft text detector weight will be downloaded to {}".format(weight_path))
        download(url=url, save_path=weight_path)

    return weight_path