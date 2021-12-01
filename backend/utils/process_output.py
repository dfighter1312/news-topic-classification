from typing import List
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

def process_multiple_output(output: np.ndarray, file_list: List, title_list: List):
    result = list()
    for cl in CLASSES:
        result.append({
            'className': cl,
            'matchedTitles': list()
        })
    print(output)
    for i, score in enumerate(output):
        label = np.argmax(score)
        result[label]['matchedTitles'].append({
            'title': title_list[i],
            'filename': file_list[i],
            'score': float(np.max(score))
        })
    return result