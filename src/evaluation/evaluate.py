import os
import sys
from typing import Tuple
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from utils.logger import logger
from utils.exception import CustomException


class EvaluateClustering:
    def __init__(self, data: pd.DataFrame, k_range: Tuple[int, int] = (2, 11)):
        """
        Initialize with data and a range of k values to evaluate.

        Args:
            data (pd.DataFrame): Feature matrix for clustering evaluation.
            k_range (Tuple[int, int]): Tuple containing min and max k values.
        """
        self.data = data
        self.k_range = k_range

    def get_best_k(self) -> int:
        """
        Compute silhouette scores for each k and return the best k.

        Returns:
            int: Optimal number of clusters based on silhouette score.
        """
        try:
            from sklearn.cluster import KMeans

            logging.info("Starting clustering evaluation...")
            scaler = StandardScaler()
            scaled_data = scaler.fit_transform(self.data)

            best_k = self.k_range[0]
            best_score = -1

            for k in range(*self.k_range):
                kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
                cluster_labels = kmeans.fit_predict(scaled_data)
                score = silhouette_score(scaled_data, cluster_labels)
                logging.info(f"k={k}, Silhouette Score={score:.4f}")

                if score > best_score:
                    best_k = k
                    best_score = score

            logging.info(f"Best k found: {best_k} with silhouette score: {best_score:.4f}")
            return best_k

        except Exception as e:
            raise CustomException(e, sys)