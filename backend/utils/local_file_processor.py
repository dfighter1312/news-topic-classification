import tensorflow as tf
from gensim.models.doc2vec import Doc2Vec
from utils.config import MODEL_PATH, DOC2VEC_PATH

class LocalFileProcessor(object):

    def save_model(self, model):
        pass

    def load_model(self, model: tf.keras.Model):
        return model.load_weights(MODEL_PATH)

    def load_doc2vec(self):
        model = Doc2Vec.load(DOC2VEC_PATH)
        return model