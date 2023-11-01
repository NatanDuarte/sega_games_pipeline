import pandas as pd
from src.logger import Logger


class Extractor:
    def __init__(self, logger:Logger) -> None:
        self.logger = logger

    def run(self, csv_path:str):
        self.logger.info('reading csv data')
        df = pd.read_csv(csv_path)
        return df
