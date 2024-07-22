# importing libraries
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
import sys,os
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

from src.utils import(save_object,
                      load_numpy_array_data)

from src.entity.artifact_entity import(DataTransformationArtifact,
                                       ModelTrainingArtifacts)
from src.entity.config_entity import ModelTrainingConfig
from src.constants.training_pipeline import *

"""
creating model_trainer component by using data_transformation_artifact and
as inputs and model_training_artifacts as output
    
"""
class ModelTrainer:
    def __init__(self,
                 data_transformation_artifact:DataTransformationArtifact,
                 model_training_config:ModelTrainingConfig): 
        
        self.data_transformation_artifact = data_transformation_artifact
        self.model_training_config = model_training_config

    def initiate_model_training(self):
        try:
            # importing x_train and y_train from data transformation artifacts
            x_train = load_numpy_array_data(self.data_transformation_artifact.x_train_filepath)
            y_train = load_numpy_array_data(self.data_transformation_artifact.y_train_filepath)
            logging.info('imported x_train and y_train')

            linear_regression = LinearRegression()
            
            # fitting x_train and y_train to random forest model
            model = linear_regression.fit(x_train, y_train)
            logging.info('fit the linear_regression model to x_train and y_train')

            # saving the model 
            save_object(
                file_path = self.model_training_config.model_training_file_path,
                obj = model
            )
            logging.info('saved the model')

            # model training artifacts
            model_training_artifacts = ModelTrainingArtifacts(
                model_filepath = self.model_training_config.model_training_file_path
            )
            logging.info('file path saved in model training artifacts')
            return model_training_artifacts

        except Exception as e:
            logging.info('error occured in initiate_model_training module')
            raise CustomException(e,sys)