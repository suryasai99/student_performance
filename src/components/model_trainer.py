import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import datatransformation
from src.utils import save_object,evaluate_model
from dataclasses import dataclass
from sklearn.linear_model import Ridge,ElasticNet,Lasso,LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

@dataclass
class Modeltrainconfig:
    trained_model = os.path.join('artifacts/model.pkl')

class Model_trainer:
    def __init__(self):
        self.t_model = Modeltrainconfig()
    def training(self,train_path,test_path):
        try:
            logging.info('taking the transformed data')
            x_train,x_test,y_train,y_test = datatransformation.initiated_data_transformation(train_path,test_path)

            models = {
                'linear regressor':LinearRegression(),
                'random forest Regressor':RandomForestRegressor(),
                'xgboost Regressor':XGBRegressor(),
                'ridge':Ridge(),
                'lasso':Lasso(),
                'elastic net':ElasticNet()
            }

            logging.info('evaluating the model')
            result = evaluate_model(x_train,x_test,y_train,y_test,models)
            max_value = max(result)

            print(f'The best model is {max_value} and r2score is {models[max_value]}')

            logging.info('saving the model')
            save_object(file_path=self.t_model.trained_model,
                        obj = models[max_value])

        except Exception as e:
            logging.info('error occured in model training')
            raise CustomException(e,sys)