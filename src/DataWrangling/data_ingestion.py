import os
import shutil
from kagglehub import dataset_download
from utils.logger import logger
from utils.exception import CustomException


class DataIngestion:
    def __init__(self):
        self.kaggle_dataset_id = "vjchoudhary7/customer-segmentation-tutorial-in-python"
        self.artifact_dir = os.path.join("artifacts", "data_ingestion")
        os.makedirs(self.artifact_dir, exist_ok=True)

    def download_and_save_data(self):
        try:
            # Step 1: Download dataset using kagglehub (saved in kagglehub cache)
            logger.info("Downloading dataset from KaggleHub...")
            dataset_path = dataset_download(self.kaggle_dataset_id)

            logger.info(f"Dataset downloaded to Kaggle cache: {dataset_path}")

            # Step 2: Find CSV file(s) and copy to artifacts folder
            for file in os.listdir(dataset_path):
                if file.endswith(".csv"):
                    src = os.path.join(dataset_path, file)
                    dest = os.path.join(self.artifact_dir, file)
                    shutil.copy(src, dest)
                    logger.info(f"Copied {file} to {self.artifact_dir}")

            return self.artifact_dir

        except Exception as e:
            logger.error("Failed during data ingestion.")
            raise CustomException(e)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.download_and_save_data()
