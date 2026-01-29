import sys
from dataclasses import dataclass, asdict
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from src.exception import CustomException
from src.logger import logging

TARGET_COLUMN = "cluster"


@dataclass
class PCAconfig:
    n_components: int = 2
    random_state: int = 42


class CreateCluster:
    def __init__(self):
        self.pcaconfig = PCAconfig()
        self.pca = PCA(**asdict(self.pcaconfig))
        self.kmeans = KMeans(n_clusters=3, random_state=42)

    def fit(self, preprocessed_data: pd.DataFrame) -> pd.DataFrame:
        """
        Fit PCA + KMeans on TRAIN data only
        """
        try:
            logging.info("Fitting PCA and KMeans on training data")

            reduced = self.pca.fit_transform(preprocessed_data)    # here we have one the pca only for the clutering to work better
            labels = self.kmeans.fit_predict(reduced)

            df = preprocessed_data.copy()
            df[TARGET_COLUMN] = labels

            return df

        except Exception as e:
            raise CustomException(e, sys)

    def fit_test(self, preprocessed_data: pd.DataFrame) -> pd.DataFrame:
        """
        Predict clusters for TEST / NEW data
        """
        try:
            logging.info("Predicting clusters for new data")

            reduced = self.pca.transform(preprocessed_data)
            labels = self.kmeans.predict(reduced)

            df = preprocessed_data.copy()
            df[TARGET_COLUMN] = labels

            return df

        except Exception as e:
            raise CustomException(e, sys)
