import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## Initialize the data ingestion configuration

@dataclass
class dataingestionconfig:
    train_data_path = os.path.join('artifacts/train.csv')
    test_data_path = os.path.join('artifacts/test.csv')

class Dataingestion:
    def __init__(self):
        self.data = dataingestionconfig()
    def initiate_data_ingestion(self):
        try:
            logging.info('initiating the data ingestion')
            os.makedirs('artifacts',exist_ok=True)

            df = pd.read_csv(os.path.join('artifacts/data.csv'))

            logging.info('dividing the data into train and test')
            train,test = train_test_split(df,
                                          test_size=0.25,
                                          random_state=42)
            

            train.to_csv(self.data.train_data_path,
                         index = False,
                         header = True)
            test.to_csv(self.data.test_data_path,
                        index = False,
                        header = True)
            
            logging.info('data ingestion completed')

            return(self.data.train_data_path,
                   self.data.test_data_path)

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        
if __name__=='__main__':
    sk = Dataingestion()
    sk.initiate_data_ingestion()
