import tensorflow as tf
from core.model.base_model import BaseModel


class CNN(BaseModel):

    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Conv1D(16, kernel_size=3, activation='relu', input_shape=(50, 1)),
            tf.keras.layers.MaxPool1D(pool_size=2),
            tf.keras.layers.Conv1D(32, kernel_size=3, activation='relu'),
            tf.keras.layers.MaxPool1D(pool_size=2),
            tf.keras.layers.Conv1D(64, kernel_size=3, activation='relu'),
            tf.keras.layers.MaxPool1D(pool_size=2),
            tf.keras.layers.Conv1D(128, kernel_size=3, activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(256, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(5, activation='softmax')
        ])

    def fit(self, **kwargs):
        self.model.fit(**kwargs)

    def compile(self, **kwargs):
        self.model.compile(**kwargs)

    def predict(self, X):
        return self.model.predict(X)