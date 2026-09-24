import os 
import requests
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

current_parent_path = Path(__file__).resolve().parent.parent
csv_path = current_parent_path / "csv_files"

load_dotenv()

# Getting google sheet information
sheet_id = os.getenv("sheet_id")
sheet_name = os.getenv("sheet_name")


# Exporting google sheet
export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"



# Getting current date
current_date = datetime.now().strftime("%Y_%m_%d")

# Creating function to download csv
def download_csv():
    print("Connecting to Google Sheets")

    # getting request from exporting url 
    response = requests.get(export_url)
    if response.status_code == 200:
        output_path = f"{csv_path}/updated_finance_numbers_{current_date}.csv"

        # os.makedirs(folder_path, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Successfully downloaded csv file and saved to {os.path.abspath(output_path)}")
    else: 
        print(f"Failed to donwload csv file: {response.status_code}")

if __name__ == "__main__":
    download_csv()
