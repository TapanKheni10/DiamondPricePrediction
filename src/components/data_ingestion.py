import os 
import sys
## Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

## Get the parent directory (src's parent) and add it to the path
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

import logger_
import exception

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## Initialize the Data Ingestion configuration

## Is a place holder to create the classes
## It helps us to create class variables directly without __init__ method
@dataclass 
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")

## Data Ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger_.logging.info("Data Ingestion method starts")
        try:
            df = pd.read_csv(os.path.join("notebooks/data", "gemstone.csv"))
            logger_.logging.info("Dataset read as pandas Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logger_.logging.info("Raw data is created")

            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            # os.makedirs(os.path.join(self.ingestion_config.train_data_path), exist_ok=True)
            # os.makedirs(os.path.join(self.ingestion_config.test_data_path), exist_ok=True)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logger_.logging.info("Ingestion of Data is completed.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

            
        except Exception as e:
            logger_.logging.info("Exception occured at data ingestion stage")
            raise exception.CustomException(e, sys)