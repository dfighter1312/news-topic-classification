import numpy as np
from utils.read_ckpts import load_model
from core.model.news_model import NewsTextModel
from core.data.text_process import text_process
from core.data.dataset import Dataset
from sklearn.model_selection import train_test_split
from utils.process_output import process_output, process_multiple_output


class Execution(object):

    model = NewsTextModel()

    def train(self):
        self.dataset = Dataset()

        # Split the dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(
            self.dataset.X,
            self.dataset.y,
            test_size=0.2
        )

        # Do training steps

        # Save the model
        # save_model(None)
        return str(X_train)

    def test(self, request, multiple: bool):
        """
        Predict the text label.
        If the request contains multiple article, set multiple to True
        """
        file_list = list()
        title_list = list()
        X = list()
        if multiple:
            file_list = [r["filename"] for r in request]
            title_list = [r["title"] for r in request]
            X = [r["title"] + r["body"] for r in request]
        else:
            X = [request["title"] + ' ' + request["body"]]
        X_transformed = text_process(X)

        # Get the trained model
        load_model(self.model.model)

        # Do prediction steps (prediction must return 
        # a probability prediction for each topic)
        result = self.model.predict(X_transformed)
        if multiple:
            result = process_multiple_output(result, file_list, title_list)
        else:
            result = process_output(result)
        return result