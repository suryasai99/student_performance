import os
from datetime import datetime
from src.constants.training_pipeline import *
from datetime import datetime

# class for creating folder of artifact
class TrainingPipelineConfig:
    def __init__(self):     
        self.artifact_dir:str = os.path.join(ARTIFACT_DIR)

"""
    Data Ingestion configurations(filepaths)

"""
class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        self.data_ingestion_dir:str = os.path.join(
            training_pipeline_config.artifact_dir, 
            DATA_INGESTION_DIR_NAME
        )

        self.original_data_filepath:str = os.path.join(
            training_pipeline_config.artifact_dir, 
            ORIGINAL_DATA_FILENAME
        )


        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, 
            TRAIN_FILE_NAME
        )

        self.testing_file_path:str = os.path.join(
            self.data_ingestion_dir, 
            TEST_FILE_NAME
        )

"""
    Data Transformation configurations(filepaths)

"""

class DataTransformationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        self.data_transformation_dir:str = os.path.join(
            training_pipeline_config.artifact_dir, 
            DATA_TRANSFORMATION_DIR_NAME
        )

        self.x_train_filepath = os.path.join(
            self.data_transformation_dir,
            TRAIN_DIR_NAME,
            X_TRAIN_FILE_PATH
        )

        self.y_train_filepath = os.path.join(
            self.data_transformation_dir,
            TRAIN_DIR_NAME,
            Y_TRAIN_FILE_PATH
        )

        self.x_test_filepath = os.path.join(
            self.data_transformation_dir,
            TEST_DIR_NAME,
            X_TEST_FILE_PATH
        )

        self.y_test_filepath = os.path.join(
            self.data_transformation_dir,
            TEST_DIR_NAME,
            Y_TEST_FILE_PATH
        )

        self.preprocessor_filepath = os.path.join(
            self.data_transformation_dir,
            PREPROCESSOR_FILE_PATH
        )

"""
    Model Training configurations(filepaths)

"""
class ModelTrainingConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        self.model_training_file_path:str = os.path.join(
            training_pipeline_config.artifact_dir, 
            MODEL_TRAINING_DIR_NAME,
            MODEL_FILE_PATH
        )

"""
    Model Evaluation configurations(filepaths)

"""
class ModelEvaluationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        self.time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

        self.model_evaluation_file_path:str = os.path.join(
            training_pipeline_config.artifact_dir, 
            MODEL_EVALUATION_DIR_NAME,
            self.time_stamp,
            MODEL_EVALUATION_REPORT_FILEPATH    
        )    