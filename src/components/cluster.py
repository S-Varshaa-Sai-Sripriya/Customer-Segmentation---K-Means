import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from utils.logger import logger
from utils.exception import CustomException

class KMeansClustering:
    def __init__(self, n_clusters: int = 3, random_state: int = 42):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)

    def fit_predict(self, X: pd.DataFrame) -> np.ndarray:
        try:
            logger.info("Fitting KMeans model")
            cluster_labels = self.model.fit_predict(X)
            logger.info("KMeans model fitted and clusters predicted")
            return cluster_labels
        except Exception as e:
            logger.error(f"Error in KMeans fit_predict: {str(e)}")
            raise CustomException(e)

    def get_silhouette_score(self, X: pd.DataFrame) -> float:
        try:
            labels = self.model.labels_
            score = silhouette_score(X, labels)
            logger.info(f"Silhouette Score: {score}")
            return score
        except Exception as e:
            logger.error(f"Error in computing silhouette score: {str(e)}")
            raise CustomException(e)