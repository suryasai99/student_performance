from dataclasses import dataclass 


"""
    Data Ingestion ARTIFACTS

"""
@dataclass
class DataIngestionArtifact:
    train_filepath:str
    test_filepath:str

"""
    Data Transformation ARTIFACTS 

"""

@dataclass
class DataTransformationArtifact:
    x_train_filepath:str
    y_train_filepath:str
    x_test_filepath:str 
    y_test_filepath:str
    preprocessor_filepath:str

"""
    Model Training ARTIFACTS 

"""

@dataclass
class ModelTrainingArtifacts:
    model_filepath:str