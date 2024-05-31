import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import Dataingestion 
from src.components.data_transformation import datatransformation
from src.components.model_trainer import Model_trainer

if __name__=='__main__':
    D_I = Dataingestion()
    train_path,test_path = D_I.initiate_data_ingestion()
    print(train_path, test_path)
    #data_transformation = datatransformation()

    #x_train_arr,x_test_arr,y_train_arr,y_test_arr=data_transformation.initiated_data_transformation(train_path,test_path)
    #print(x_train_arr.head())
    mt = Model_trainer()
    mt.training(train_path,test_path)

