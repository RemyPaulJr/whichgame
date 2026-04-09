import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

rawg_api = os.getenv("RAWG_API")

url = f"https://api.rawg.io/api/games?key={rawg_api}"

response = requests.get(url)

today = datetime.now().strftime("%Y%m%d")

folder_path = "raw_ingest"
file_name = f"games_{today}.json"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

full_path = os.path.join(folder_path, file_name)

if response.status_code == 200:
    print("Success!")
    games_dict = response.json()

    with open(full_path, "w", encoding="utf-8") as file:
        json.dump(games_dict, file, indent=4, ensure_ascii=False)

    print(f"games_{today}.json file saved.")
else:
    print("Failed: ", response.status_code)
 
