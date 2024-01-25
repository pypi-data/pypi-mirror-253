import json
from pathlib import Path
from typing import Callable, Iterable

import numpy as np
import xmltodict
from PIL import Image
from tqdm import tqdm

from detecty.bbox import BBox

p2p = Callable[[Path], Path]
pf2p = Callable[[Path, str], Path]


def yolo_to_bbs(imgs: Iterable[Path], img_2_txt: p2p, max_bbs=2):
    for path in imgs:
        try:
            img = Image.open(path)
            with open(img_2_txt(path)) as f:
                bbs = [
                    BBox.from_yolo(
                        [float(v) for v in line.split()[1:]],
                        img.size)
                    for line in f]

                if len(bbs) > max_bbs:
                    continue

                yield path, max(bbs, key=lambda bb: bb.area)
        except Exception:
            pass


def coco_to_bbs(coco_json: str | Path):
    with open(coco_json) as f:
        coco = json.load(f)
        imgs = coco['images']
        anns = coco['annotations']
        anns = {ann['image_id']: ann for ann in anns}

        for img in imgs:
            ann = anns[img['id']]
            yield img['file_name'], BBox.from_xywh(ann['bbox'])


def xml_to_bbs(xmls: Iterable[Path], xml2img: pf2p):
    for xml in xmls:
        with open(xml) as f:
            try:
                d = xmltodict.parse(f.read())
                ann = d['annotation']
                bb = ann['object']['bndbox']
                path = xml2img(xml, ann['filename'])
                yield path, BBox.from_dict(bb)
            except Exception:
                pass


def data_jsonl():
    with open('data.jsonl', 'w') as out:
        def dump(path: Path, bb: BBox):
            record = json.dumps({
                'path': str(path),
                'bbox': bb.dict})

            print(record, file=out)

        root = Path('data/israeli-plate-ocr')
        with open(root / 'records.jsonl') as f:
            for line in tqdm(f):
                record = json.loads(line)
                path = root / record['car']
                bb = BBox.from_dict(record['plate_bbox'])
                dump(path, bb)

        #
        with open('data/car-plates-ocr/data/train.json') as f:
            records = json.load(f)

        for record in tqdm(records):
            try:
                path = Path('data/car-plates-ocr/data') / record['file']
                Image.open(path)
                nums = record['nums']
                if len(nums) > 1:
                    continue

                bb = nums[0]['box']
                bb = np.array(bb)
                bb = BBox.from_xyxyxyxy(bb)
                dump(path, bb)
            except Exception:
                pass

        #
        root = Path('data/egyptian-cars-plates/EALPR Vechicles dataset/')
        imgs = root / 'Vehicles'

        data = yolo_to_bbs(
            imgs.rglob('*.jpg'),
            lambda path: root / 'Vehicles Labeling' / f'{path.stem}.txt')

        for path, bb in tqdm(data):
            dump(path, bb)

        #
        root = Path('AllCarsDataset672')
        with open('data/deeblpd2020/LPD20Annotation.txt') as f:
            for line in tqdm(f):
                try:
                    path, bb = line.split()
                    bb = json.loads(bb)
                    path = root / path.replace('\\', '/').replace("'", "")
                    path = Path('data/deeblpd2020') / path
                    bb = BBox.from_xywh(bb)
                    dump(path, bb)
                except Exception:
                    pass

        #
        root = Path('data/car-licence-plate-detection-yolo/licence-plates')
        for path, bb in tqdm(xml_to_bbs(
                root.rglob('*.xml'),
                lambda path, file: path.parent.parent / 'images' / file)):
            dump(path, bb)

        #
        root = Path('data/number-plate-detection')
        for path, bb in tqdm(xml_to_bbs(
                root.rglob('*.xml'),
                lambda path, file: path.parent / file)):
            dump(path, bb)

        #
        root = Path('data/indian-vehicle-dataset')
        for path, bb in tqdm(xml_to_bbs(
                root.rglob('*.xml'),
                lambda path, file: path.parent / file)):
            try:
                Image.open(path)
                dump(path, bb)
            except Exception:
                pass

        #
        root = Path('data/car-plate-detection')
        ann = root / 'annotations'
        img = root / 'images'
        for path, bb in tqdm(xml_to_bbs(
                root.rglob('*.xml'),
                lambda _, file: img / file)):
            dump(path, bb)

        #
        root = Path('data/car-license-plate-detection-iran/train/')
        ann = root / '_annotations.coco.json'
        for file, bb in tqdm(coco_to_bbs(ann)):
            path = root / file
            dump(path, bb)

        #
        root = Path('data/car-license-plate-detection-iran/valid/')
        ann = root / '_annotations.coco.json'
        for file, bb in tqdm(coco_to_bbs(ann)):
            path = root / file
            dump(path, bb)
            dump(path, bb)
