import pandas as pd
from pathlib import Path
from datetime import datetime
from config.settings import logger

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
