import os

from .seed import setseed
from . import config

setseed()
if config.no_cuda:
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
