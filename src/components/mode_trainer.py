import sys 
import os 
from src.exception import CustomException
from src.logger import logging
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble  import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from src.utils import save_object,evaluate_model
from sklearn.metrics import accuracy_score
from dataclasses import dataclass



@dataclass
class ModelTrainerConfig:
    trained_model_file=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer=ModelTrainerConfig()


    def initiate_model_trainning(self,train_arr,test_arr):
        try:

            logging.info(
                "Model Trainning has started "
            )
            x_train,y_train,x_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1],


            )
            models = {
                        "RandomForest": RandomForestClassifier(),
                        "KNN": KNeighborsClassifier(),
                        "LogisticRegression": LogisticRegression(),
                        "AdaBoost": AdaBoostClassifier(),
                        "GradientBoosting": GradientBoostingClassifier(),
                        "XGB": XGBClassifier(),
                            "CatBoost": CatBoostClassifier(verbose=False)
                        }
            
            
                



        

            model_report:dict=evaluate_model(models,x_train,y_train,x_test,y_test)



            


            

            # to get best score from the dict
            best_model_name=max(model_report,key=model_report.get)

            best_model_score=model_report[best_model_name]
            best_model=models[best_model_name]



            y_predict=best_model.predict(x_test)
            print(best_model_name)
            print(accuracy_score(y_test,y_predict))
           

            if best_model_score < 0.6:
                raise CustomException(" didnt found the best model")
            
            logging.info("WE found the best model")

            


            save_object(
                file_path=self.model_trainer.trained_model_file,
                obj=best_model
            )














        except Exception as e:
            raise CustomException(e,sys)

