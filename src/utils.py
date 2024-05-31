import os,sys
from src.logger import logging
from src.exception import CustomException
import pickle as pkl
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok = True) 
        with open(file_path, "wb") as file_obj:
            pkl.dump(obj,file_obj)
            
    except Exception as e:
        logging.info('error occured in utils.save_object')
        raise CustomException(e,sys)
    
def evaluate_model(x_train,x_test,y_train,y_test,models):
    try:
        report = {}
        for keys,values in models.item():
            model = values.fit(x_train,y_train)
            y_pred = model.predict(x_test)
            r2score = r2_score(y_test,y_pred)
            report.update({keys:r2score})

        return report

    except Exception as e:
        logging.info('error occured in utils.evaluate_model')
        raise CustomException(e,sys)

