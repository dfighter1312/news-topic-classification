import re
from utils.local_file_processor import LocalFileProcessor
from nltk.corpus import stopwords

def text_process(text, local_file_processor: LocalFileProcessor):
    text = preprocessing(text)
    d2v_model = local_file_processor.load_doc2vec()
    v = d2v_model.infer_vector(text)
    return v

def preprocessing(inp):
  text = str(inp)
  tokens = [re.sub(r'[^(a-z|A-Z)]', '', word.strip().lower()) for word in text.split()]
  tokens = [word for word in tokens if word not in stopwords.words('english')]

  return tokens