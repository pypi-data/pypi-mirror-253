
from PIL import Image, ImageDraw, ImageFile

from detecty.bbox import BBox

ImageFile.LOAD_TRUNCATED_IMAGES = True


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


def crop(img: Image.Image, bbox: BBox, h_margin=0.1, v_margin=.3):
    w = bbox.width
    h = bbox.height
    x1 = int(bbox.x1 - h_margin * w)
    y1 = int(bbox.y1 - v_margin * h)
    x2 = int(bbox.x2 + h_margin * w)
    y2 = int(bbox.y2 + v_margin * h)
    return img.crop((x1, y1, x2, y2))
