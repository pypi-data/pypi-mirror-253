from dataclasses import dataclass
from pathlib import Path

import torch
from PIL import Image, ImageDraw, ImageFile
from torch import Tensor, nn
from torchvision.models import MobileNet_V2_Weights, mobilenet_v2
from torchvision.transforms.functional import (pad, resize, to_grayscale,
                                               to_tensor)

from detecty.bbox import BBox
from detecty.util import crop

ImageFile.LOAD_TRUNCATED_IMAGES = True
TARGET_SIZE = 256


class DetectionModule(nn.Module):
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
            nn.Linear(1280, 4))

    def forward(self, x):
        return self.net(x)


def draw_bbox(img: Image.Image, *bboxs: BBox):
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    for color, bb in zip(colors, bboxs):
        draw.rectangle(
            (bb.x1, bb.y1, bb.x2, bb.y2),
            outline=color,
            width=1)

    return img


def pre_process(img: Image.Image | Tensor):
    img = to_tensor(to_grayscale(img))

    _, h, w = img.shape
    ratio = TARGET_SIZE / max(h, w)

    img = resize(
        img,
        [round(h * ratio), round(w * ratio)],
        antialias=True)

    _, h, w = img.shape
    img = pad(img, [0, 0, max(0, h-w), max(0, w-h)])

    return img


@dataclass(kw_only=True)
class DetectionResult:
    bbox: BBox
    plate: Image.Image


class Detection:
    def __init__(self):
        def fix_state_dict(state_dict):
            return {
                k.replace('net.net', 'net'): v
                for k, v in state_dict.items()}

        from importlib.resources import files
        from io import BytesIO

        import detecty

        ckpt = torch.load(
            BytesIO(files(detecty).joinpath('model.ckpt').read_bytes()),
            map_location=torch.device('cpu'))

        self.model = DetectionModule()
        self.model.load_state_dict(fix_state_dict(ckpt['state_dict']))
        self.model.eval()

    def __call__(self, img: Image.Image):
        x = pre_process(img)

        with torch.inference_mode():
            y = self.model(x.unsqueeze(0)).squeeze(0)

        bbox = BBox.from_tensor(y)
        bbox = bbox.scale(max(img.size) / TARGET_SIZE)

        return DetectionResult(
            bbox=bbox,
            plate=crop(img, bbox))
