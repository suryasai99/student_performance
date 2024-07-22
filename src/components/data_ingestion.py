# importing libraries
import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from src.constants.training_pipeline import *
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig

"""
ingesting original data and splitting data into train and test
    
"""
class DataIngestion:
    def __init__(self, 
                 data_ingestion_config:DataIngestionConfig): 
        self.data_ingestion_config = data_ingestion_config

    @staticmethod
    def read_data(file_path):
        try:
            logging.info(f'reading the csv file from file path:{file_path}')
            return pd.read_csv(file_path)
        
        except Exception as e:
            logging.info(f'error occured while reading the csv file from file path:{file_path}')
            return CustomException(e,sys)    

    def initiate_data_ingestion(self):
        try:
            # reading the original data
            df = DataIngestion.read_data(self.data_ingestion_config.original_data_filepath)
            logging.info(f'original Dataset imported into dataframe from csv file{df.head()}')

            # dividing training and testing data
            train_data,test_data = train_test_split(df, 
                                                    test_size = TRAIN_TEST_SPLIT_RATIO, 
                                                    random_state = RANDOM_STATE)
            logging.info('divided train and test data')
            
            # In case If we dont have artifacts folder. we need to create it
            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path), exist_ok = True)


            # saving it in the artifacts path
            train_data.to_csv(self.data_ingestion_config.training_file_path, 
                              index = False,
                              header = True)
            
            test_data.to_csv(self.data_ingestion_config.testing_file_path,
                             index = False,
                             header = True)
            logging.info('saved train and test data to csv')
            
            # saving the artifacts
            data_ingestion_artifact = DataIngestionArtifact(
                train_filepath = self.data_ingestion_config.training_file_path,
                test_filepath = self.data_ingestion_config.testing_file_path
            )
            
            logging.info('train and test path sent to data ingestion artifacts')

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e,sys)

