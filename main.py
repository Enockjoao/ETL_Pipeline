import pandas as pd
import os
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


log_file = Path("etl_pipeline.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def extract(file_path: str) -> Optional[pd.DataFrame]:
    
    try:
        pd.options.display.max_rows = 10
        file_path = Path(file_path)

        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return None
        
        logger.info(f"Starting data extraction from file: {file_path}")
        df = pd.read_csv(file_path)

        if df.empty:
            logger.warning(f"The file {file_path} is empty.")
            return None
        
        logger.info(f"Data successfully extracted. Total records: {len(df)}")
        return df
    
    except Exception as e:
        logger.error(f"Error during extraction: {str(e)}")
        return None

def transform(df: pd.DataFrame) -> Optional[pd.DataFrame]:
   
    try:
        if df is None:
            logger.warning("Input DataFrame is None. Skipping transformation.")
            return None

        logger.info("Starting data transformation")

        initial_records = len(df)
        
        df_clean = df.dropna()
        after_nulls_removed = len(df_clean)

        df_clean = df_clean.drop_duplicates()
        final_records = len(df_clean)

        logger.info(f"Initial records: {initial_records}")
        logger.info(f"Records removed (null values): {initial_records - after_nulls_removed}")
        logger.info(f"Records removed (duplicates): {after_nulls_removed - final_records}")
        logger.info(f"Final records: {final_records}")

        if final_records == 0:
            logger.warning("All records were removed after cleaning!")
            return None

        return df_clean
    
    except Exception as e:
        logger.error(f"Error during transformation: {str(e)}")
        return None

def save(df: pd.DataFrame, output_path: str) -> None:
   
    try:
        if df is None:
            logger.warning("No data to save.")
            return
        
        output_path = Path(output_path)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = output_path.with_name(f"{output_path.stem}_{timestamp}{output_path.suffix}")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        
        logger.info(f"File successfully saved at: {output_path}")
    
    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")

def main(input_file: str, output_file: str) -> None:
    
    try:
        logger.info("Starting ETL pipeline")

        df = extract(input_file)
        transformed_df = transform(df)
        save(transformed_df, output_file)

        logger.info("ETL pipeline successfully completed")
    
    except Exception as e:
        logger.error(f"ETL pipeline error: {str(e)}")

if __name__ == "__main__":
    input_file = r"C:\Users\tr302137\Desktop\Project_Folder\python\raw\MOCK_DATA.csv"
    output_file = r"C:\Users\tr302137\Desktop\Project_Folder\python\processed\transformed_data.csv"
    
    main(input_file, output_file)