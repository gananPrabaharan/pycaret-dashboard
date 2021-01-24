from os.path import dirname, join
import json


class Paths:
    FLASK_APP_PATH = (dirname(dirname(__file__)))
    PROJECT_PATH = dirname(FLASK_APP_PATH)
    REACT_APP_PATH = join(PROJECT_PATH, 'react_app')
    LOGS = join(FLASK_APP_PATH, "logs")


config_file_path = join(Paths.PROJECT_PATH, 'config.json')
with open(config_file_path) as json_file:
    config = json.load(json_file)


class Deployment:
    HOST = config.get('Deployment').get('HOST')
    FLASK_PORT = int(config.get('Deployment').get('FLASK_PORT'))
    NGINX_PORT = int(config.get('Deployment').get('NGINX_PORT'))
