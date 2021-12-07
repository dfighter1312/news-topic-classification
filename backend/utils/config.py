# Path configurations
TRAIN_PATH: str = 'data_sample/train.csv'
PRED_PATH: str = 'results/'
CKPT_PATH: str = 'ckpts/'

MODEL_FILE: str = 'checkpoint'
DOC2VEC_FILE: str = 'd2v.model'
GLOVE_FILE: str = 'glove.6B.100d.txt'
TOKENIZER_FILE: str = 'tokenizer.json'

MODEL_PATH: str = CKPT_PATH + MODEL_FILE
DOC2VEC_PATH: str = CKPT_PATH + DOC2VEC_FILE
GLOVE_PATH: str = CKPT_PATH + GLOVE_FILE
TOKENIZER_PATH: str = CKPT_PATH + TOKENIZER_FILE

# Data configurations
TARGET_COLUMN = 'Class Index'
CLASSES = ["Business", "Culture", "Politics", "Sport", "Technology"]

# Model configurations
MAX_LEN: int = 500
EMBED_VECTOR_LEN: int = 100