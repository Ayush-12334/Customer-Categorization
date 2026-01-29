import sys 
import os
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.components.data_clustering import CreateCluster, TARGET_COLUMN
from src.utils import save_object

class DatatranformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:   
    def __init__(self):
        self.data_transformation_config = DatatranformationConfig()

    def feature_engineering(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Started feature engineering")
        try:
            df = df.copy()
            today = datetime.today()

            # ---- Age ----
            if 'Year_Birth' in df.columns:
                df['Age'] = today.year - df['Year_Birth']

            # ---- Education (Safe mapping) ----
            if 'Education' in df.columns:
                edu_map = {"Basic": 0, "2n Cycle": 1, "Graduation": 2, "Master": 3, "PhD": 4}
                df['Education'] = df['Education'].map(edu_map).fillna(2).astype(int)

            # ---- Marital Status (Safe mapping) ----
            if 'Marital_Status' in df.columns:
                mar_map = {"Married": 1, "Together": 1, "Absurd": 0, "Widow": 0,
                           "YOLO": 0, "Divorced": 0, "Single": 0, "Alone": 0}
                df['Marital_Status'] = df['Marital_Status'].map(mar_map).fillna(0).astype(int)

            # ---- Children & Parental Status ----
            if {'Kidhome', 'Teenhome'}.issubset(df.columns):
                df['Children'] = df['Kidhome'] + df['Teenhome']
                df['Parental Status'] = np.where(df['Children'] > 0, 1, 0)

            # ---- Total Spending ----
            spending_cols = ['MntWines', 'MntFruits', 'MntMeatProducts',
                             'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
            available_spend = [c for c in spending_cols if c in df.columns]
            if available_spend:
                df['Total_Spending'] = df[available_spend].sum(axis=1)

            # ---- Days as Customer ----
            if 'Dt_Customer' in df.columns:
                df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce',format='%d-%m-%Y')
                # Fill NaT with a default date before calculating days
                df['Dt_Customer'] = df['Dt_Customer'].fillna(df['Dt_Customer'].mode()[0])
                df['Days_as_Customer'] = (today - df['Dt_Customer']).dt.days

            # Drop non-numeric/original columns
            drop_cols = ['Year_Birth', 'Kidhome', 'Teenhome', 'Dt_Customer', 'ID', 'Z_CostContact', 'Z_Revenue']
            df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True)

            return df
        except Exception as e:
            raise CustomException(e, sys)

    def get_transformer_object(self, train_set: pd.DataFrame, test_set: pd.DataFrame):
        try:
            logging.info("Initiating ColumnTransformer")
            
            # Match columns exactly as they appear in the engineered DataFrame
            outlier_features = [col for col in ["MntWines","MntFruits","MntMeatProducts","Age","Total_Spending"] if col in train_set.columns]
            numeric_features = [col for col in train_set.columns if train_set[col].dtype != 'O' and col not in outlier_features]

            numeric_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            outlier_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("power", PowerTransformer(standardize=True))
            ])

            preprocessor = ColumnTransformer([
                ("num", numeric_pipeline, numeric_features),
                ("out", outlier_pipeline, outlier_features)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def intiate_data_transformation(self, train_path_data, test_data_path):
        try:
            train_df = pd.read_csv(train_path_data)
            test_df = pd.read_csv(test_data_path)

            train_df = self.feature_engineering(train_df)
            test_df = self.feature_engineering(test_df)

            preprocessor = self.get_transformer_object(train_df, test_df)

            # The output here is a NumPy Array
            X_train_arr = preprocessor.fit_transform(train_df)
            X_test_arr = preprocessor.transform(test_df)

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )

            # IMPORTANT: Many Clustering functions expect DataFrames or specific Indexing
            # We convert the transformed array back to a DataFrame before passing to CreateCluster
            X_train_df = pd.DataFrame(X_train_arr)
            X_test_df = pd.DataFrame(X_test_arr)

            cluster_creator = CreateCluster()
            cluster_creator = CreateCluster()

            # ✅ FIT ONLY ON TRAIN
            label_train_df = cluster_creator.fit(preprocessed_data=X_train_df)

            # ✅ PREDICT USING SAME OBJECT
            label_test_df = cluster_creator.fit_test(preprocessed_data=X_test_df)

            
            
            train_arr = np.c_[
                label_train_df.drop(columns=[TARGET_COLUMN]).values, 
                label_train_df[TARGET_COLUMN].values
            ]
            test_arr = np.c_[
                label_test_df.drop(columns=[TARGET_COLUMN]).values, 
                label_test_df[TARGET_COLUMN].values
            ]

            logging.info("Transformation and Clustering completed.")
            return train_arr, test_arr

        except Exception as e:
            raise CustomException(e, sys)