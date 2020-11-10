import pandas as pd
import numpy as np

import optuna 

import xgboost

train = pd.read_csv("./data/train.csv", nrows=3e6, 
                        dtype={'row_id': 'int64', 
                        'timestamp': 'int64', 
                        'user_id': 'int32', 
                        'content_id': 'int16', 
                        'content_type_id': 'int8',
                        'task_container_id': 'int16', 
                        'user_answer': 'int8', 
                        'answered_correctly': 'int8', 
                        'prior_question_elapsed_time': 'float64', 
                        'prior_question_had_explanation': 'boolean'},
                        )

class DataPipeline:
    def __init__(self):
        self.is_fitted = False

    def fit(self, X, y=None):
        self.is_fitted = True
        raise NotImplementedError
    
    def transform(self, X, y=None):
        if self.is_fitted == True:
            return 1
        else:
            kdsjkjksh

    def func(self):
        pass
