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

from components import data_ingestion

if __name__ == "__main__":
    obj = data_ingestion.DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print("Train data path, Test data path: ", train_data_path, test_data_path)