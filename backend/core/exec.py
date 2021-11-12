from core.data.text_process import text_process
from core.data.dataset import Dataset
from sklearn.model_selection import train_test_split
from utils.local_file_processor import LocalFileProcessor


class Execution(object):

    localfile = LocalFileProcessor()

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
        self.localfile.save_model(None)
        return str(X_train)

    def test(self, X):
        X_transformed = text_process(X)

        # Get the trained model
        model = self.localfile.get_model()

        # Do prediction steps (prediction must return 
        # a probability prediction for each topic)
        result = model.predict(X_transformed)
        return result