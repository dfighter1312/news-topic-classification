from flask import Flask, request

from core.exec import Execution

app = Flask(__name__)
execution = Execution()

@app.route("/")
def index():
    """Provide simple health check route."""
    return "<p>Hello!</p>"

@app.route("/v1/train", methods=["GET"])
def fit():
    result = execution.train()
    # Test by printing all the training dataset
    return result

@app.route("/v1/predict", methods=["POST", "GET"])
def predict():
    execution.test(None)
    return None