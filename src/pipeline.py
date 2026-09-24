import os 
import requests 
from dotenv import load_dotenv

# Getting google sheet information
sheet_id = os.getenv("sheet_id")
sheet_name = os.getenv("sheet_name")


# Exporting google sheet
export_url = f"https://google.com{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Creating function to download csv