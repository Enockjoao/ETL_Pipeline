import sys
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from config.settings import logger
from src.extract import extract
from src.transform import transform
from src.load import save

def run_pipeline(input_file: str, output_file: str) -> None:
    try:
        logger.info("Starting ETL pipeline")

        df = extract(input_file)
        transformed_df = transform(df)
        save(transformed_df, output_file)

        logger.info("ETL pipeline successfully completed")
    
    except Exception as e:
        logger.error(f"ETL pipeline error: {str(e)}")

if __name__ == "__main__":
    input_file = r"C:\Users\tr302137\Desktop\Pasta_de_projeto\etl_pipeline\data\raw\MOCK_DATA.csv"
    output_file = r"C:\Users\tr302137\Desktop\Pasta_de_projeto\etl_pipeline\data\processed\Processed.csv"
    
    run_pipeline(input_file, output_file)
