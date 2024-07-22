# importing libraries
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.entity.config_entity import(TrainingPipelineConfig,
                                     DataIngestionConfig,
                                     DataTransformationConfig,
                                     ModelTrainingConfig) 
                          
from src.entity.artifact_entity import(DataIngestionArtifact,
                                       DataTransformationArtifact,
                                       ModelTrainingArtifacts)
import os,sys

"""
creating Training pipeline by using the components of 
data_ingestion,data_transformation,model_trainer
    
"""
class TrainPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        #self.data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)

    def start_data_ingestion(self) -> DataIngestionArtifact :
        try:
            logging.info('Data ingestion started')
            data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f'Data ingestion finished and artifact: {data_ingestion_artifact}')
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_transformation(self, 
                                  data_ingestion_artifact:DataIngestionArtifact) -> DataTransformationArtifact:
        try:
            logging.info('Data transformation initiated')
            data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(
                data_ingestion_artifact = data_ingestion_artifact,
                data_transformation_config = data_transformation_config
            )

            data_transformation_artifact = data_transformation.initiate_data_transformation()
            
            logging.info(f'Data transformation finished and artifact: {data_transformation_artifact}')
            return data_transformation_artifact
        
        except Exception as e:
            raise CustomException(e,sys)   

    def start_model_training(self,
                             data_transformation_artifact:DataTransformationArtifact):
        try:
            logging.info("model training initiated")
            model_training_config = ModelTrainingConfig(self.training_pipeline_config)
            
            model_training = ModelTrainer(
                data_transformation_artifact = data_transformation_artifact,
                model_training_config = model_training_config    
            )

            model_training_artifact = model_training.initiate_model_training()
            logging.info("model training successfull")
            return model_training_artifact
        
        except Exception as e:
            raise CustomException(e,sys) 
                
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact)
            model_training_artifact = self.start_model_training(data_transformation_artifact)
        
        except Exception as e:
            raise CustomException(e,sys)


if __name__=='__main__':
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()

