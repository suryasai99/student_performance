import os,sys
from src.logger import logging
from src.exception import CustomException
import pickle as pkl

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok = True) 
        with open(file_path, "wb") as file_obj:
            pkl.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)