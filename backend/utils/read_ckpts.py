import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from utils.config import *

def read_glove_vector():
    with open(GLOVE_PATH, 'r', encoding='UTF-8') as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            w_line = line.split()
            curr_word = w_line[0]
            word_to_vec_map[curr_word] = np.array(w_line[1:], dtype=np.float64)

    emb_matrix = np.zeros((get_vocab_len(), EMBED_VECTOR_LEN))
    words_to_index = get_word_index_map()

    for word, index in words_to_index.items():
        embedding_vector = word_to_vec_map.get(word)
        if embedding_vector is not None:
            emb_matrix[index, :] = embedding_vector
    
    return emb_matrix

def load_model(model: tf.keras.Model):
    return model.load_weights(MODEL_PATH)

def read_tokenizer():
    with open(TOKENIZER_PATH) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    return tokenizer

def get_vocab_len():
    return len(read_tokenizer().word_index) + 1

def get_word_index_map():
    return read_tokenizer().word_index