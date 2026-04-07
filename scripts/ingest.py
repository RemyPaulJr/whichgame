import requests
import os
from dotenv import load_dotenv

load_dotenv()

rawg_api = os.getenv("RAWG_API")

url = f"https://api.rawg.io/api/games?key={rawg_api}"

response = requests.get(url)

if response.status_code == 200:
    print("Success!")
    games_dict = response.json()
    print(games_dict)
else:
    print("Failed: ", response.status_code)
 