import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object

class Predictpipeline:
    def __init__(self):
        pass
    def predictdata(self,features):
        try:
            model_path = os.path.join('artifacts/model.pkl')
            preprocessor_path = os.path.join('artifacts/preprocessor.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            predict = model.predict(data_scaled)

            return predict



        except Exception as e:
            logging.info('error occured in predict pipeline in Predictpipeline class and Predictdata method')
            raise CustomException(e,sys)
        
class Customdata:
    def __init__(self,
                 gender,
                 race_ethnicity,
                 parental_level_of_education,
                 lunch,
                 test_preparation_course,
                 reading_score,
                 writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def intodf(self):
        try:
            data = {
                'gender':[self.gender],
                'race_ethnicity':[self.race_ethnicity],
                'parental_level_of_education':[self.parental_level_of_education],
                'lunch':[self.lunch],
                'test_preparation_course': [self.test_preparation_course],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score]
            }

            convert_df = pd.DataFrame(data)
            logging.info('data converted into dataframe')

            return convert_df
            
        except Exception as e:
            logging.info('error occured in predict pipeline in customdf class and intodf method')
            raise CustomException(e,sys)