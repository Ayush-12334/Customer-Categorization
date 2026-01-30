import os
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,f1_score,roc_curve,precision_score,recall_score,confusion_matrix
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from src.exception import CustomException
from src.logger import logging
import dill
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)


        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

        
def evaluate_model(model_taining,x_train,y_train,x_test,y_test)->dict:

    
    report={}
    try:
        logging.info("Evaluation of the model has started ")
        

        for model_name, model in model_taining.items():
            logging.info(f"Currently training: {model_name}")

            model.fit(x_train,y_train)
            y_predict=model.predict(x_test)

            score=accuracy_score(y_test,y_predict)
            


            report[model_name]=score


            


        logging.info("Evaluation has been completed")


        return report
    

    except Exception as e:
        raise CustomException(e,sys)



        