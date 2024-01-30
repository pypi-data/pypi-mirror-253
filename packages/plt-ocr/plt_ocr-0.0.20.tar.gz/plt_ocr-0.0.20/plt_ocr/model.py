from dataclasses import dataclass

import torch
from PIL import Image
from torch import Tensor, nn
from torchvision.models import MobileNet_V2_Weights, mobilenet_v2
from torchvision.transforms.functional import (pad, resize, to_grayscale,
                                               to_tensor)

CHARS = '0123456789'
NUM_CLASSES = len(CHARS) + 1
NA = NUM_CLASSES - 1
MAX_PLATE_LEN = 8

TARGET_HEIGHT = 128
TARGET_WIDTH = 256


def pre_process(img: Image.Image | Tensor):
    img = to_grayscale(img)
    img = to_tensor(img)

    _, h, w = img.shape
    ratio = min(TARGET_HEIGHT / h, TARGET_WIDTH / w)
    img = resize(img, [round(h * ratio), round(w * ratio)], antialias=True)

    _, h, w = img.shape
    img = pad(img, [0, 0, TARGET_WIDTH - w, TARGET_HEIGHT - h])

    return img


class OCRModule(nn.Module):
    def __init__(self, weights: MobileNet_V2_Weights | None = None):
        super().__init__()
        net = mobilenet_v2(weights=weights)
        net.features[0][0] = nn.Conv2d(
            1, 32,
            kernel_size=3,
            stride=2,
            padding=1,
            bias=False)

        net.classifier = nn.Identity()  # type: ignore

        self.net = nn.Sequential(
            net,
            nn.Linear(1280, NUM_CLASSES * MAX_PLATE_LEN))

    def forward(self, x):
        out = self.net(x)
        return out.reshape(-1, NUM_CLASSES, MAX_PLATE_LEN)


def fix_state_dict(state_dict):
    return {
        k.replace('net.net', 'net'): v
        for k, v in state_dict.items()}


def load_from_model_ckpt():
    from importlib.resources import files
    from io import BytesIO

    import plt_ocr

    ckpt = torch.load(
        BytesIO(files(plt_ocr).joinpath('model.ckpt').read_bytes()),
        map_location=torch.device('cpu'))

    model = OCRModule()
    model.load_state_dict(fix_state_dict(ckpt['state_dict']))

    return model


@dataclass
class OCRResult:
    prediction: str
    confidence: float


class OCR:
    def __init__(self):
        def fix_state_dict(state_dict):
            return {
                k.replace('net.net', 'net'): v
                for k, v in state_dict.items()}

        from importlib.resources import files
        from io import BytesIO

        import plt_ocr

        ckpt = torch.load(
            BytesIO(files(plt_ocr).joinpath('model.ckpt').read_bytes()),
            map_location=torch.device('cpu'))

        self.model = OCRModule()
        self.model.load_state_dict(fix_state_dict(ckpt['state_dict']))
        self.model.eval()

    def __call__(self, img: Image.Image):
        x = pre_process(img)

        with torch.inference_mode():
            logits = self.model(x.unsqueeze(0)).squeeze(0)

        prob = logits.softmax(dim=0).squeeze()
        prob = torch.max(prob, dim=0).values

        confidence = 10 ** prob.log10().sum().item()

        pred = logits.argmax(dim=0).squeeze()
        pred = [CHARS[v] for v in pred.tolist() if v < NA]
        pred = ''.join(str(v) for v in pred)

        return OCRResult(pred, confidence)


def fire(plate_path: str):
    import json
    img = Image.open(plate_path)
    model = OCR()
    result = model(img)
    print(json.dumps(result.__dict__))


def main():
    from fire import Fire
    Fire(fire)
