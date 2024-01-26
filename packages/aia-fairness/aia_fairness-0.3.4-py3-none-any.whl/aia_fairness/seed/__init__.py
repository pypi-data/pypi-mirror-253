import numpy as np
import torch
import silence_tensorflow.auto
import tensorflow as tf
import random

from ..config import random_state

def setseed():
    np.random.seed(random_state)
    torch.manual_seed(random_state)
    tf.random.set_seed(random_state)
    tf.keras.utils.set_random_seed(random_state)
    random.seed(random_state)
