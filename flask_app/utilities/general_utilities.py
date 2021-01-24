from shutil import copyfile
from constants.general_constants import Paths
from os.path import join
from services.log import setup_logger


def setup():
    """
    Copy config folder from backend to frontend (having the same config to avoids redundancy)

    :return:
    """
    react_src_folder = join(Paths.REACT_APP_PATH, "src")
    project_config = join(Paths.PROJECT_PATH, 'config.json')
    react_config = join(react_src_folder, 'config.json')
    copyfile(project_config, react_config)

    setup_logger()


def check_bool(string_value):
    """
    Checks whether a string value should be converted to a True/False

    :param string_value: (string) value we wish to convert to a boolean
    :return: (boolean) boolean conversion of string
    """
    if string_value is True or string_value.lower() == "true" or string_value.lower() == "yes":
        return True
    return False
