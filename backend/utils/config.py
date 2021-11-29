# Path configurations
TRAIN_PATH: str = 'data_sample/train.csv'
PRED_PATH: str = 'results/'
CKPT_PATH: str = 'ckpts/'

MODEL_FILE: str = 'my_checkpoint'
DOC2VEC_FILE: str = 'd2v.model'

MODEL_PATH: str = CKPT_PATH + MODEL_FILE
DOC2VEC_PATH: str = CKPT_PATH + DOC2VEC_FILE

# Data configurations
TARGET_COLUMN = 'Class Index'

CLASSES = ["Business", "Culture", "Politics", "Sport", "Technology"]