import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging


class DataIngestion:
    def __init__(self):
        self.raw_data_path = os.path.join("data", "raw", "SMSSpamCollection")
        self.processed_data_path = os.path.join("data", "processed", "cleaned_data.csv")

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion")

            df = pd.read_csv(self.raw_data_path, sep='\t', header=None, names=["label", "message"])

            logging.info("Raw data loaded successfully")

            df.to_csv(self.processed_data_path, index=False)
            logging.info("Cleaned data saved to processed folder")

            return self.processed_data_path

        except Exception as e:
            raise CustomException(e)