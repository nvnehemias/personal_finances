import csv
import json  
from get_path import get_project_root
from database_connection import get_connection

# Obtaining file path
base_dir = get_project_root()
csv_file_path = base_dir / "csv_files"
sql_path = base_dir / "sql" / "load_data.sql" 

# Finding all files with .json 
all_csv_files = list(csv_file_path.glob("updated_finance_numbers_*.csv"))

# connecting to database
conn = get_connection()
cursor = conn.cursor()

# Open SQL files
with open(sql_path, "r", encoding="utf-8") as sql_file:
    sql_script = sql_file.read()

for f in all_csv_files:
    print(f"Loading file: {f.name}")

    try: 
        with open(f,"r",encoding = 'utf-8-sig') as file:
            # Loading file
            data = csv.DictReader(file)    

            for i in data:
                # 1. Strip spaces from keys and values instantly
                i = {key.strip(): (val.strip() if val else "") for key, val in i.items()} 
                
                # 2. Automatically turn ANY empty string field into None (SQL NULL)
                cleaned_row = {key: (None if val == "" else val) for key, val in i.items()}


                # FIX: Read directly from cleaned_row instead of i
                values = (
                    cleaned_row["ID"],
                    cleaned_row["Source"],
                    cleaned_row["Amount"],  # This will now correctly pass None instead of ""
                    cleaned_row["Note"],
                    cleaned_row["Sub Note"],
                    cleaned_row["Transaction Date"],
                    cleaned_row["Date Range"],
                    cleaned_row["Owner"]
                )
                print("Executing data load to database.")
                cursor.execute(sql_script,values)                

    except FileNotFoundError:
        print(f"File not found: {f.name}")

     
conn.commit() 
cursor.close()
conn.close()