import os.path as osp
from setuptools import setup, find_packages
from typing import List

REQUIRED = ['torch',
            'torchvision',
            'tqdm',
            'tensorboardX',
            'thop',
            'segmentation_models_pytorch @ git+https://github.com/qubvel/segmentation_models.pytorch',
            'timm>=0.4',
            'imgaug',
            'ml_collections',
            'easydict']

setup(
    name='SegTran',
    version='0.0.1',
    packages=find_packages(),
    install_requires=REQUIRED
)
