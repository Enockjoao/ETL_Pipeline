import pandas as pd
from pathlib import Path
from typing import Optional
from config.settings import logger

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
