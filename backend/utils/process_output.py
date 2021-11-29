import numpy as np
from utils.config import CLASSES

def process_output(output: np.ndarray):
    result = list()
    for i in range(len(CLASSES)):
        obj = {
            'className': CLASSES[i],
            'bestClass': bool(np.argmax(output) == i),
            'score': float(output[0][i])
        }
        result.append(obj)
    return result