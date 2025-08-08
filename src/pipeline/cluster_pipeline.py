import pandas as pd
import os

from utils.logger import get_logger
from utils.exception import CustomException
from components.cluster import KMeansClustering

logger = get_logger(__name__)

class ClusterPipeline:
    def __init__(self, data: pd.DataFrame, output_path: str = "artifacts/final_clusters.csv"):
        self.data = data
        self.output_path = output_path

    def run(self, n_clusters: int = 3) -> pd.DataFrame:
        try:
            logger.info("Starting Clustering Pipeline")

            clustering_model = KMeansClustering(n_clusters=n_clusters)
            self.data['Cluster'] = clustering_model.fit_predict(self.data)

            silhouette = clustering_model.get_silhouette_score(self.data.drop(columns=['Cluster']))
            logger.info(f"Final Silhouette Score: {silhouette:.4f}")

            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            self.data.to_csv(self.output_path, index=False)
            logger.info(f"Clustered data saved to {self.output_path}")

            return self.data

        except Exception as e:
            logger.error("Error in clustering pipeline")
            raise CustomException(e)