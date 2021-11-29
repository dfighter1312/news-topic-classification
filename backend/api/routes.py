import json

from flask import Flask, request
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
from flask_expects_json import expects_json

from core.exec import Execution
from api.request_model import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
execution = Execution()

@app.route("/")
def index():
    """Provide simple health check route."""
    return "<p>Hello!</p>"

@app.route("/v1/prototype/predict")
@cross_origin()
def prototype_predict():
    import random
    classNames = ['Sport','Food','Business','Travel','Medical','Trend','Culture','Lifestyle','Companies','Places']
    classPoints = {x: random.random() for x in classNames}
    return classPoints


@app.route("/v1/train", methods=["GET"])
def fit():
    result = execution.train()
    # Test by printing all the training dataset
    return result

@app.route("/v1/predict", methods=["POST", "GET"])
# @expects_json(schema=predict_single_request, ignore_for=["GET"])
def predict():
    r = request.get_json()
    result = execution.test(r)
    return json.dumps(result)