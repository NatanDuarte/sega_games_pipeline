import pandas as pd

from src.etl.extractor import Extractor
from src.logger import Logger


class Pipeline:
    def __init__(self, csv_path:str, logger:Logger) -> None:
        self.logger = logger
        self.csv_path = csv_path

    def run(self):
        extractor = Extractor(logger=self.logger)
        df = extractor.run(csv_path=self.csv_path)
        print(df.head())
