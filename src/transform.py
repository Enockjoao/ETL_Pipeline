import pandas as pd
from typing import Optional
from config.settings import logger

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
