import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
#from src.components.data_ingestion import Dataingestion
from src.utils import save_object
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

@dataclass
class datatransformationconfig:
    preprocessor_file_path = os.path.join('artifacts/preprocessor.pkl')

  
class datatransformation:
    def __init__(self):
        self.transformation = datatransformationconfig()  

    def initiated_data_transformation(self,train_path,test_path):
         try:
            logging.info('reading train and test files')
            x_train = pd.read_csv(os.path.join(train_path))
            x_test = pd.read_csv(os.path.join(test_path))

            logging.info('data transformation initiated')
            input_train = x_train.drop('math_score',axis = 1)
            output_train = x_train['math_score']
            input_test = x_test.drop('math_score',axis = 1)
            output_test =  x_test['math_score']

            logging.info('dividing numerical and categorical columns')
            num_cols = [i for i in input_train.columns if input_train[i].dtype == 'int64']
            cat_cols = [i for i in input_train.columns if input_train[i].dtype == 'object']

            logging.info('using column transformer with the pipelines ')
            
            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median'))
                    ('scaler',StandardScaler())
                ]
            )
                
            cat_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )

            preprocessor = ColumnTransformer([
                ('cat',cat_pipeline,cat_cols),
                ('num',num_pipeline,num_cols)
                
            ])

            logging.info('fitting the preprocessing pipeline to the data ')
            input_train = pd.DataFrame(preprocessor.fit_transform(input_train))
            input_test = pd.DataFrame(preprocessor.transform(input_test))

            logging.info('saving the preprocessor model')
            save_object(file_path = self.transformation.preprocessor_file_path,
                        obj = preprocessor)
            logging.info('Processsor pickle in created and saved')

            return(input_train,
                   input_test,
                   output_train,
                   output_test)

         except Exception as e:
             logging.info('error occured in data transformation')
             raise CustomException(e,sys)
