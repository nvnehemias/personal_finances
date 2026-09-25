import pandas as pd
import json  
from get_path import get_project_root
from database_connection import get_connection

# Obtaining file path
base_dir = get_project_root()
csv_file_path = base_dir / "csv_files" 

# Finding all files with .json 
all_csv_files = list(csv_file_path.glob("updated_finance_numbers_*.csv"))

# connecting to database
conn = get_connection()
cursor = conn.cursor()

for f in all_csv_files:
    print(f"Loading file: {f.name}")

    try: 
        with open(f,"r",encoding = 'utf-8') as file:
            # Loading file
            data = pd.read_csv(file)    

    except FileNotFoundError:
        print(f"File not found: {f.name}")

     
conn.commit() 
cursor.close()
conn.close()