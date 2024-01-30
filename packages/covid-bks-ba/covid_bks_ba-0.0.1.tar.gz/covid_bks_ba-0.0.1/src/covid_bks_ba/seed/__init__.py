import numpy as np
import random

from ..config import random_state

def setseed():
    np.random.seed(random_state)
    random.seed(random_state)
