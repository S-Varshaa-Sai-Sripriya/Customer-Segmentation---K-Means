from src.DataWrangling.data_ingestion import DataIngestion
from src.DataWrangling.data_preprocessing import DataPreprocessor
from src.DataWrangling.data_transformation import DataTransformer
from pathlib import Path

# Ingest data
raw_data_path = Path("artifacts/data/raw/customer_data.csv")
data_ingestor = DataIngestion()
data_ingestor.download_dataset()

# Preprocess
preprocessor = DataPreprocessor()
df_clean = preprocessor.preprocess(raw_data_path)
preprocessor.save_preprocessed_data(Path("artifacts/data/processed/cleaned_data.csv"))

# Transform
transformer = DataTransformer()
df_transformed = transformer.transform(df_clean)
df_transformed.to_csv("artifacts/data/processed/transformed_data.csv", index=False)
