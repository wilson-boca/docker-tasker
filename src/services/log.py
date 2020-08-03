import os
from pathlib import Path
from loguru import logger


class CustomLogger(object):
    def __init__(self):
        self.path = '{}/static'.format(Path(os.path.abspath(os.path.dirname(__file__))).parent)
        file = '{}/details.log'.format(self.path)
        open(file, 'w').close()
        logger.add(file, backtrace=True, diagnose=True)

    @staticmethod
    def get_logger():
        return logger


log = CustomLogger().get_logger()
