import tensorflow as tf
from core.model.base_model import BaseModel
from utils.read_ckpts import read_glove_vector, read_tokenizer
from utils.config import EMBED_VECTOR_LEN, MAX_LEN


class NewsTextModel(BaseModel):

    def __init__(self):
        tokenizer = read_tokenizer()
        words_to_index = tokenizer.word_index
        self.model = create_model(
            input_dim=len(words_to_index) + 1,
            output_dim=EMBED_VECTOR_LEN,
            max_length=MAX_LEN
        )

    def fit(self, **kwargs):
        self.model.fit(**kwargs)

    def compile(self, **kwargs):
        self.model.compile(**kwargs)

    def predict(self, X):
        return self.model.predict(X)


def create_model(filters = 10, kernel_size = 3, 
                input_dim = None, output_dim=300, max_length = None):

    emb_matrix = read_glove_vector()

    # Channel 1D CNN
    input = tf.keras.Input(shape=(max_length,))
    embeddding1 = tf.keras.layers.Embedding(input_dim=input_dim, 
                            output_dim=output_dim, 
                            input_length=max_length, 
                            input_shape=(max_length, ),
                            # Assign the embedding weight with word2vec embedding marix
                            weights = [emb_matrix],
                            # Set the weight to be not trainable (static)
                            trainable = False)(input)
    conv1 = tf.keras.layers.Conv1D(filters=filters, kernel_size=kernel_size, activation='relu', 
                kernel_constraint= tf.keras.constraints.MaxNorm(max_value=3, axis=[0,1]))(embeddding1)
    pool1 = tf.keras.layers.MaxPool1D(pool_size=2, strides=2)(conv1)
    conv2 = tf.keras.layers.Conv1D(filters=filters*2, kernel_size=kernel_size, activation='relu', 
                kernel_constraint= tf.keras.constraints.MaxNorm(max_value=3, axis=[0,1]))(pool1)
    pool2 = tf.keras.layers.MaxPool1D(pool_size=2, strides=2)(conv2)
    conv3 = tf.keras.layers.Conv1D(filters=filters*4, kernel_size=kernel_size, activation='relu', 
                kernel_constraint= tf.keras.constraints.MaxNorm(max_value=3, axis=[0,1]))(pool2)
    pool3 = tf.keras.layers.MaxPool1D(pool_size=2, strides=2)(conv3)
    flat1 = tf.keras.layers.Flatten()(pool3)
    drop1 = tf.keras.layers.Dropout(0.3)(flat1)
    dense1 = tf.keras.layers.Dense(40, activation='relu')(drop1)
    drop2 = tf.keras.layers.Dropout(0.3)(dense1)
    dense2 = tf.keras.layers.Dense(40, activation='relu')(drop2)
    drop3 = tf.keras.layers.Dropout(0.3)(dense2)
    dense3 = tf.keras.layers.Dense(40, activation='relu')(drop3)
    drop4 = tf.keras.layers.Dropout(0.3)(dense3)
    dense4 = tf.keras.layers.Dense(40, activation='relu')(drop4)
    
    # Interpretation
    outputs = tf.keras.layers.Dense(5, activation='softmax')(dense4)
    model = tf.keras.Model(inputs=input, outputs=outputs)
    
    # Compile
    model.compile( loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    print(model.summary())
    return model