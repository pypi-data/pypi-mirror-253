from pathlib import Path

import torch
from PIL import Image, ImageDraw, ImageFile
from torch import Tensor
from torchvision.transforms.functional import resize, to_grayscale, to_tensor


def clear_tmp():
    from os import mkdir
    from shutil import rmtree
    rmtree('tmp', ignore_errors=True)
    mkdir('tmp')
