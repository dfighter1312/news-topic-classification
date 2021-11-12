from abc import abstractmethod, ABC


class BaseModel(ABC):

    @abstractmethod
    def __init__(self, __C):
        """Initialization."""
        raise NotImplementedError

    @abstractmethod
    def compile(self):
        """
        Compile the model by defining loss function and optimizer.
        """
        raise NotImplementedError

    @abstractmethod
    def fit(self):
        """Fit the model."""
        raise NotImplementedError

    @abstractmethod
    def predict(self):
        """Predict result from the model."""
        raise NotImplementedError