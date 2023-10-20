import logging

from logging import Logger


class Logger():

    @staticmethod
    def get_logger() -> Logger:
        logging_format = '%(asctime)s | %(funcName)s: %(levelname)s: %(message)s'
        logging.basicConfig(level=logging.INFO, format=logging_format)
        return logging.getLogger()
