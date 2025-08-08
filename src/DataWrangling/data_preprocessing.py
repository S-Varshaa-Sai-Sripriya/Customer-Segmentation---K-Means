import pandas as pd
from sklearn.preprocessing import StandardScaler
from utils.logger import logger
from utils.exception import CustomException

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            logger.info("Starting data preprocessing...")
            df_cleaned = df.dropna()
            df_scaled = pd.DataFrame(self.scaler.fit_transform(df_cleaned), columns=df_cleaned.columns)
            logger.info("Preprocessing complete.")
            return df_scaled
        except Exception as e:
            raise CustomException("Error during preprocessing", e)
