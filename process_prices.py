import json
import os
import polars as pl
from datetime import datetime


# Load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# Extracts ID, prices, and timestamp from the latest prices data
def extract_prices(data, ts):
    price_list = []
    for item_id, item_data in data['data'].items():
        price_list.append({
            'id': item_id,
            'high_price': item_data['high'],
            'low_price': item_data['low'],
            'timestamp': ts
        })
    return price_list


# Directory containing the current price JSON files
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "output")

# Path to the processed files log
log_file_path = os.path.join(data_dir, "processed_files.log")

# Ensuring the output directory really exists
os.makedirs(data_dir, exist_ok=True)

# Loads the list of processed files
if os.path.exists(log_file_path):
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        processed_files = log_file.read().splitlines()
else:
    processed_files = []

# List to store all the extracted prices
all_prices = []

# Each JSON file in the directory processed
for json_filename in os.listdir(data_dir):
    if json_filename.endswith(".json") and json_filename not in processed_files:
        json_file_path = os.path.join(data_dir, json_filename)
        file_data = load_json(json_file_path)
        # Extracts the timestamp from the filename
        try:
            ts_str = json_filename.replace('.json', '')
            ts = datetime.strptime(ts_str, "%Y%m%d%H%M")
        except ValueError as e:
            print(f"Skipping file {json_filename} due to timestamp parsing error: {e}")
            continue
        extracted_prices = extract_prices(file_data, ts)
        all_prices.extend(extracted_prices)
        # Mark the file as processed
        processed_files.append(json_filename)

# Saves the updated list of processed files
with open(log_file_path, 'w', encoding='utf-8') as log_file:
    for processed_file in processed_files:
        log_file.write(f"{processed_file}\n")

# Converts the list of prices to a Polars Dframe
df = pl.DataFrame(all_prices)

# Converts 'timestamp' column to datetime if not already
df = df.with_column(pl.col("timestamp").str.strptime(pl.Datetime, format="%Y%m%d%H%M"))

# Sorts data by item ID and timestamp
df = df.sort(by=['id', 'timestamp'])

# Saves the aggregated data to a new CSV file
output_file_path = os.path.join(data_dir, "aggregated_item_prices.csv")
df.write_csv(output_file_path)
print(f"Aggregated data saved to {output_file_path}")
