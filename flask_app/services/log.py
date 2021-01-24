import logging
from logging.handlers import TimedRotatingFileHandler
import os
from constants.general_constants import Paths


def setup_logger():
    if not os.path.exists(Paths.LOGS):
        os.makedirs(Paths.LOGS)

    filename = os.path.join(Paths.LOGS, "pycaret_dashboard.log")

    # Daily rotating log file with 10 backups
    timed_handler = TimedRotatingFileHandler(filename=filename, when="midnight", interval=1, backupCount=10)
    timed_handler.suffix = "%Y%m%d"

    # Formatter to include file name, function name, timestamp, log level, message
    formatter = logging.Formatter(
        'File Name: %(filename)s, Function Name: %(funcName)s, DateTime: %(asctime)s,'
        'Log Level: %(levelname)s - %(message)s'
    )
    timed_handler.setFormatter(formatter)

    # gets existing instance or creates a new one
    logger = logging.getLogger(__name__)

    # logging level is INFO, so all INFO, WARNING, ERROR, and CRITICAL level messages will be logged
    logger.setLevel(logging.INFO)

    logger.addHandler(timed_handler)
    return logger


def get_logger():
    return logging.getLogger(__name__)
