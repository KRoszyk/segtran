import os.path as osp
from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    requirements_path = osp.join(osp.dirname(osp.abspath(__file__)), 'requirements.txt')
    with open(requirements_path) as f:
        return [line for line in f.read().splitlines() if not line.startswith('#')]
      
setup(
    name='segtran',
    version=0.0.1,
    packages=find_packages(),
    install_requires=get_requirements()
)
