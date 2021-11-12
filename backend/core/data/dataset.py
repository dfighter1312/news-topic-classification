from typing import Tuple
import numpy as np
import pandas as pd
from core.data.text_process import text_process
from utils.config import TRAIN_PATH, TARGET_COLUMN

class Dataset(object):

    def __init__(self):
        data = pd.read_csv(TRAIN_PATH)
        self.column = None
        self.index = None
        self.X, self.y = self.preprocess(data)

    def preprocess(self, data: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        X = text_process(data.drop(TARGET_COLUMN, axis=1)).values
        y = data[[TARGET_COLUMN]].values
        return X, y