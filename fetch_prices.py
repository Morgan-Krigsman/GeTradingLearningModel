import requests
import requests_cache
import time
import json
import os
from datetime import datetime

# caching to store responses for 1 hour
requests_cache.install_cache('osrs_cache', expire_after=3600)

# Base URL
base_url = "https://prices.runescape.wiki/api/v1/osrs"

# User-Agent
headers = {
    "User-Agent": "Trade-app/1.0 (@Puggstein)"
}


# fetch data with rate limiting and custom User-Agent
def fetch_data(endpoint):
    url = base_url + endpoint

    # Send GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
        return None


# Save data to a file
def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"File created: {filename}")


# Determine the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specifiy the sub-folder within the script's directory
output_dir = os.path.join(script_dir, "output")
os.makedirs(output_dir, exist_ok=True)

while True:
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Fetch and save the latest prices
    latest_prices = fetch_data("/latest")
    if latest_prices:
        latest_prices_file = os.path.join(output_dir, f"{timestamp}.json")
        save_to_file(latest_prices, latest_prices_file)
        print("Latest prices query successful")

    # Wait for 5 minutes before making the next request
    time.sleep(300)
