# 🚀 ETL Pipeline with Python and Pandas  

This project is a simple yet effective ETL (Extract, Transform, Load) pipeline built with Python and Pandas.  
It extracts data from a CSV file, processes it (removing null values and duplicates), and saves the transformed data to a new CSV file—all while logging key operations for easy debugging. 🛠️  

## 📌 Features  

✅ **Extraction:** Reads data from a CSV file into a Pandas DataFrame.  
✅ **Transformation:** Cleans data by removing null values and duplicates.  
✅ **Loading:** Saves the processed data into a new CSV file with a timestamp.  
✅ **Logging:** Provides detailed logs for tracking the ETL process and debugging errors.  

## 📂 Project Structure  

📦 etl-pipeline ┣ 📜 etl_pipeline.py # Main ETL script ┣ 📜 etl_pipeline.log # Log file (generated automatically) ┣ 📜 MOCK_DATA.csv # Sample input data ┗ 📜 README.md # Documentation

bash
Copiar
Editar

## 🛠 Setup and Usage  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/etl-pipeline.git
cd etl-pipeline
2️⃣ Install Dependencies
Ensure you have Python installed (preferably version 3.8+), then install the required package:

bash
Copiar
Editar
pip install pandas
3️⃣ Configure Input and Output Paths
Open etl_pipeline.py and update these variables in the main() function if needed:

python
Copiar
Editar
input_file = r"C:\Users\your_user\path\to\MOCK_DATA.csv"
output_file = r"C:\Users\your_user\path\to\transformed_data.csv"
4️⃣ Run the ETL Pipeline
bash
Copiar
Editar
python etl_pipeline.py
🔍 Logging Configuration
This script uses advanced logging with rotating file handlers to manage log files efficiently.
The log file (etl_pipeline.log) will:

Rotate when it reaches 5MB (keeping up to 3 backups).
Log messages to both the file and the console.
If needed, you can modify the logging configuration in etl_pipeline.py:

python
Copiar
Editar
log_file = Path("etl_pipeline.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3),
        logging.StreamHandler()
    ]
)
🛠️ Future Improvements
🚀 Support for additional file formats (JSON, Excel).
🚀 Implement automated unit tests for data validation.
🚀 Build a web-based UI for an easier ETL execution.


