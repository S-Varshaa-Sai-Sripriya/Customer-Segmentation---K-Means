import pandas as pd
from sklearn.decomposition import PCA
from utils.logger import logger
from utils.exception import CustomException

class DataTransformer:
    def __init__(self, n_components: int = 2):
        self.pca = PCA(n_components=n_components)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            logger.info("Starting data transformation with PCA...")
            components = self.pca.fit_transform(df)
            transformed_df = pd.DataFrame(components, columns=[f'PC{i+1}' for i in range(components.shape[1])])
            logger.info("PCA transformation complete.")
            return transformed_df
        except Exception as e:
            raise CustomException("Error during PCA transformation", e)
