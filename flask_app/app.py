from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json
from gevent.pywsgi import WSGIServer

from constants.general_constants import Deployment
from utilities.general_utilities import setup
from classes.dataset import Dataset
from services.log import get_logger
from services.models import get_model_results

logger = get_logger()

app = Flask(__name__)
CORS(app)

session_dict = {}


@app.route('/api/removeSession', methods=["POST"])
def remove_session():
    session_id = json.loads(request.form["sessionId"])
    if session_id in session_dict:
        del session_dict[session_id]

    return "Removed session", 200


@app.route('/api/upload/', methods=["POST"])
def upload_file():
    """
    Called when user uploads their file. This function parses the CSV columns into features for the front-end table

    Expected input from request:
        "file_input": csv file in request.files
    :return: list of dictionaries containing feature information. (gets converted to json)
             dictionary format: {
                 "id": int,
                "name": string,
                "include": string ("Yes" or "No"),
                "target": string ("Yes" or "No"),
            }
    """
    input_file = request.files["fileInput"]
    session_id = json.loads(request.form["sessionId"])
    input_df = pd.read_csv(input_file)

    dataset = Dataset(input_df)
    session_dict[session_id] = dataset

    feature_dict_list = [f.to_dict() for f in dataset.feature_list]
    return json.dumps(feature_dict_list), 200


@app.route('/api/import_config/', methods=["POST"])
def import_config():
    """
    Called after user finishes setting up feature configuration

    :return:
    """

    session_id = json.loads(request.form["sessionId"])
    feature_dict_list = json.loads(request.form["featureList"])

    session_dataset = session_dict.get(session_id)
    if session_dataset is None:
        logger.error("Session Id %s not found", session_id)
        raise ValueError

    session_dataset.set_features(feature_dict_list)
    return "success", 200


@app.route('/api/trainModels/', methods=["POST"])
def train_models():
    session_id = json.loads(request.form["sessionId"])
    session_dataset = session_dict.get(session_id)

    if session_dataset is None or session_dataset.train_df is None:
        logger.error("Session Id %s not found", session_id)
        raise ValueError

    target_name = session_dataset.target_feature.feature_name
    model_results = get_model_results(session_dataset.train_df, target_name)
    return "success", 200


if __name__ == "__main__":
    setup()
    # WSGIServer((Deployment.HOST, Deployment.FLASK_PORT), app).serve_forever()
    app.run(Deployment.HOST, Deployment.FLASK_PORT, debug=True)
