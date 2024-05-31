import numpy as np
import pandas as pd
import os,sys

from sklearn.base import BaseEstimator, TransformerMixin
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import Dataingestion
from src.utils import save_object
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,LabelEncoder

@dataclass
class datatransformationconfig:
    preprocessor_file_path = os.path.join('artifacts/preprocessor.pkl')

class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoders = {}
    
    def fit_transform(self, X, y=None):
        X_copy = X.copy()
        for col in X.columns:
            le = LabelEncoder()
            X_copy[col] = le.fit_transform(X_copy[col])
            self.encoders[col] = le
        return X_copy
    
    def transform(self, X):
        X_copy = X.copy()
        for col in X.columns:
            X_copy[col] = self.encoders[col].transform(X_copy[col])
        return X_copy
    
class datatransformation:
    def __init__(self):
        self.transformation = datatransformationconfig()   
    
    def transformation_pipeline(self):
        # using the transformation pipeline
            self.num_pipeline = Pipeline(
                steps =[
                    ('scaler',StandardScaler())
                ]
            )
            
            self.cat_pipeline = Pipeline(
                steps=[
                    ('scaler',StandardScaler()),
                    ('L_encoder', CustomLabelEncoder())
                ]
            )

    def initiated_data_transformation(self,x_train,x_test):
         try:
            logging.info('data transformation initiated')
            input_train = x_train.drop('math_score',axis = 1)
            output_train = x_train['math_score']
            input_test = x_test.drop('math_score',axis = 1)
            output_test =  x_test['math_score']

            logging.info('dividing numerical and categorical columns')

            num_cols = [i for i in input_train.columns if input_train[i].dtype == 'int64']
            cat_cols = [i for i in input_train.columns if input_train[i].dtype == 'object']

            # converting categorical columns  into numerical using label encoder
            #logging.info('converting categorical columns  into numerical using label encoder')
           #for i in cat_cols:
            #    label_encoder = LabelEncoder()
             #   input_train[i] = label_encoder.fit_transform(input_train[i])
              #  input_test[i] = label_encoder.transform(input_test[i])

            logging.info('using coolumn transformer with the pipelines imported from transformation_pipeline method')
            preprocessor = ColumnTransformer([
                ('num',self.num_pipeline,num_cols)
                ('cat',self.cat_pipeline,cat_cols)
            ])

            input_train = preprocessor.fit_transform(input_train)
            input_test = preprocessor.transform(input_test)

            logging.info('saving the preprocessor model')
            save_object(file_path = self.transformation.preprocessor_file_path(),
                        obj = preprocessor)

            return(input_train,
                   input_test,
                   output_train,
                   output_test)

         except Exception as e:
             logging.info('error occured in data transformation')
             raise CustomException(e,sys)
