# importing libraries
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np

from src.entity.config_entity import(ModelEvaluationConfig,
                                     ModelTrainingConfig,
                                     DataTransformationConfig,
                                     TrainingPipelineConfig) 
                          
from src.utils import(load_object,
                      load_numpy_array_data,
                      save_file_yaml)

from sklearn.metrics import(r2_score,
                            mean_absolute_error,
                            mean_squared_error,)
import os,sys


"""
evaluating the model performance on test set
    
"""
class ModelEvaluation:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        self.data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
        self.model_training_config = ModelTrainingConfig(self.training_pipeline_config)
        self.model_evaluation_config = ModelEvaluationConfig(self.training_pipeline_config)

    def metrics(self,x_test,y_test,model):
        try:
            # predicting student performance of x_test
            y_pred = model.predict(x_test)
            logging.info('predicted student performance of x_test')

            # calculating r2 score
            r2 = r2_score(y_true = y_test, 
                          y_pred = y_pred)
            
            # calculating mean squared errormean_squared_error(true,predicted))
            rmse = np.sqrt(mean_squared_error(y_true = y_test, 
                                              y_pred = y_pred))
            
            # calculating mean absolute error
            mae = mean_absolute_error(y_true = y_test, 
                                      y_pred = y_pred)
            
            logging.info(f"finished calculating r2, rmse, mae:{r2*100},{rmse},{mae}")

            report = {"r2_score" : r2*100,
                      "root_mean_squared_error":np.array(rmse), 
                      "mean_absolute_error":np.array(mae) }

            return(report)
            
        except Exception as e:
            logging.info("error occured in metrics module")
            raise CustomException(e,sys)
        
    def initiate_model_evaluation(self):
        try:
            logging.info("initiated model evaluation")
            x_test = load_numpy_array_data(self.data_transformation_config.x_test_filepath)
            y_test = load_numpy_array_data(self.data_transformation_config.y_test_filepath)
            model = load_object(self.model_training_config.model_training_file_path)

            report = self.metrics(x_test, 
                                  y_test, 
                                  model)
            logging.info("created report")

            file_path = os.path.dirname(self.model_evaluation_config.model_evaluation_file_path)
            os.makedirs(file_path, exist_ok = True)
            logging.info("model evaluation directory created")
            
            save_file_yaml(report = report, 
                           filepath = self.model_evaluation_config.model_evaluation_file_path)
            logging.info("model evaluation succesfull")

        except Exception as e:
            logging.info("error occured in initiate_model_evaluation module")
            raise CustomException(e,sys)  

if __name__ == "__main__":
    model_evaluation = ModelEvaluation()
    model_evaluation.initiate_model_evaluation()     
