import os
import sys 
from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.mode_trainer import ModelTrainer

# This class only decide where to save the data later 

# Note this class dosent store any data 
@dataclass
class DataIngestionConfig:
    train_data_path : str =os.path.join("artifacts","train.csv")   
    test_data_path : str =os.path.join("artifacts","test.csv")   
    raw_data_path : str =os.path.join("artifacts","data.csv")   


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method and component")
        try:
            df=pd.read_csv("notebooks/marketing_campaign.csv",sep='\t')
            logging.info("read the dataset as data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingestion of the data is completed")
            return (
                self.ingestion_config.test_data_path,
                self.ingestion_config.train_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ =="__main__":
    obj=DataIngestion()
    train_set,test_set=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr=data_transformation.intiate_data_transformation(train_path_data=train_set,test_data_path=test_set)
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainning(train_arr,test_arr))

