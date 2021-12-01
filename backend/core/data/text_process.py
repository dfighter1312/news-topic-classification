import re
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils.read_ckpts import read_tokenizer
from utils.config import MAX_LEN

def text_process(text):
    processed_text = [preprocessing(preprocessing(t)) for t in text]
    processed_text = np.array(processed_text)
    tokenizer = read_tokenizer()
    indices = tokenizer.texts_to_sequences(text)
    indices = pad_sequences(indices, maxlen=MAX_LEN, padding='post')
    return indices

def preprocessing(inp):
  text = str(inp)
  tokens = [re.sub(r'[^a-z|A-Z]', ' ', word.strip().lower()) for word in text.split()]

  return " ".join(tokens)