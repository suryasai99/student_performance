import pandas as pd
import numpy as np
import sys,os,pickle
from src.logger import logging
from src.exception import CustomException
import yaml

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok = True) 

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info('Exception occured in save_object function in utils.py')
        raise CustomException(e,sys)
    
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info('Exception occured in the load_object function in utils.py')
        raise CustomException(e,sys)


def save_numpy_array_data(file_path:str,
                          array:np.array):
    """
    save numpy array data to file

    Args:
        file_path (str):location of file to save
        array (np.array): np.array data to save
    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj, array)

    except Exception as e:
        logging.info('Exception occured in the save_numpy_array_data function in utils.py')
        raise CustomException(e,sys)
    

def load_numpy_array_data(file_path:str):
    """
    load numpy array data from file

    Args:
        file_path (str): location of file to load

    Returns:
        np.array: numpy array loaded
    """

    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        logging.info('Exception occured in the load_numpy_array_data function in utils.py')
        raise CustomException(e,sys)
    
def save_file_yaml(report, filepath):
    try:
        with open(filepath, 'w') as file:
            yaml.dump(report, 
                      file, 
                      default_flow_style = False)
        logging.info(f'Report successfully saved to {filepath}')

    except Exception as e:
        logging.info(f'Error occurred while saving report to {filepath}')
        raise CustomException(e, sys)