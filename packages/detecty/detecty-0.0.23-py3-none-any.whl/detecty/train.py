import json
from functools import cache
from typing import Literal, cast

import lightning as pl
import lightning.pytorch.callbacks as cb
from lightning.pytorch import loggers as pl_loggers
from PIL import Image
from pynvml.smi import nvidia_smi
from torch.nn.functional import l1_loss
from torch.optim import Adam
from torch.utils.data import DataLoader, Dataset, random_split
from torchvision.models import MobileNet_V2_Weights

from detecty.bbox import BBox
from detecty.model import TARGET_SIZE, DetectionModule, pre_process
from detecty.util import draw_bbox
from detecty.version import version


def devices(max_devices=16):
    nvsmi = cast(nvidia_smi, nvidia_smi.getInstance())

    devices = nvsmi.DeviceQuery('memory.used')
    devices = devices['gpu']
    devices = [
        i for i, d in enumerate(devices)
        if d['fb_memory_usage']['used'] < 400]

    devices = devices[:max_devices]

    return devices


class DetectionData(Dataset):
    def __init__(self, data_jsonl='data.jsonl'):
        self.data_jsonl = data_jsonl

        with open(data_jsonl) as f:
            self.records = [json.loads(line) for line in f]

    def __len__(self):
        return len(self.records)

    @cache
    def item(self, idx):
        record = self.records[idx]

        img = Image.open(record['path'])
        x = pre_process(img)
        bbox = BBox.from_dict(record['bbox'])
        d = max(img.size)
        bbox = bbox.scale(TARGET_SIZE / d)

        return x, bbox.tensor

    def __getitem__(self, idx):
        return self.item(idx)


class DetectionDataModule(pl.LightningDataModule):

    def __init__(self):
        super().__init__()
        self.data = DetectionData()
        self.train, self.valid = random_split(self.data, [0.95, 0.05])

    def train_dataloader(self):
        return DataLoader(
            self.train,
            batch_size=32,
            shuffle=True,
            num_workers=4)

    def val_dataloader(self):
        return DataLoader(
            self.valid,
            batch_size=32,
            num_workers=4)


class DetectionLightningModule(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.net = DetectionModule(MobileNet_V2_Weights.DEFAULT)

    def step(
            self, batch, batch_idx,
            name: Literal['train', 'valid'], sync_dist=False):

        x, y = batch
        y_hat = self(x)

        loss = l1_loss(y_hat, y)

        self.log(
            f'{name}/loss',
            loss,
            prog_bar=True,
            sync_dist=sync_dist)

        return loss

    def training_step(self, batch, batch_idx):
        return self.step(batch, batch_idx, 'train')

    def validation_step(self, batch, batch_idx):
        return self.step(batch, batch_idx, 'valid', sync_dist=True)

    def forward(self, x):
        return self.net(x).squeeze()

    def configure_optimizers(self):
        return Adam(self.parameters(), lr=1e-4)


def train():
    pl.seed_everything(42)

    name = 'detection'
    monitor = 'valid/loss'
    monitor_mode = 'min'

    datamodule = DetectionDataModule()
    model = DetectionLightningModule()

    logger = pl_loggers.TensorBoardLogger(
        save_dir='logs/',
        name=name,
        version=version)

    swa = cb.StochasticWeightAveraging(swa_lrs=1e-2)

    early_stopping = cb.EarlyStopping(
        monitor=monitor,
        mode=monitor_mode,
        patience=50)

    model_checkpoint = cb.ModelCheckpoint(
        save_last=False,
        save_weights_only=True,
        dirpath='ckpt',
        filename=version,
        monitor=monitor,
        mode=monitor_mode)

    trainer = pl.Trainer(
        deterministic=True,
        val_check_interval=0.25,
        accelerator='auto',
        devices=devices(),
        max_epochs=200,
        logger=logger,
        callbacks=[
            swa,
            early_stopping,
            model_checkpoint])

    trainer.fit(model, datamodule)


def clear_tmp():
    from os import mkdir
    from shutil import rmtree
    rmtree('tmp', ignore_errors=True)
    mkdir('tmp')


def sample_data():
    from torchvision.transforms.functional import to_pil_image

    clear_tmp()
    data = DetectionDataModule()
    X, Y = next(iter(data.train_dataloader()))
    for i in range(len(X)):
        img = to_pil_image(X[i])
        bbox = BBox.from_tensor(Y[i])
        draw_bbox(img, bbox).save(f'tmp/{i}.jpg')


if __name__ == '__main__':
    sample_data()
