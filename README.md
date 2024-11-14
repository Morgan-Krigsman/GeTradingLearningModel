RuneScape Item Price Prediction Using Machine Learning

Overview

This project aims to predict price fluctuations of items in RuneScape, a popular MMORPG game, using machine learning techniques. By leveraging the game’s price API, we collect historical pricing data, process and aggregate it, and then train a machine learning model to forecast future item prices. This tool can be valuable for players interested in trading and investing within the game economy.

Features

•	Automated Data Collection: Fetches the latest item prices from the RuneScape price API every 5 minutes.
•	Data Processing: Aggregates collected data into a structured format suitable for analysis.
•	Machine Learning Model: Utilizes a Random Forest Regressor to predict future high and low prices of items.
•	Scalable Architecture: Modular scripts allow for easy customization and extension.

Project Structure

•	fetch_prices.py: Fetches the latest item prices from the RuneScape API and saves them as timestamped JSON files.
•	process_prices.py: Processes the fetched JSON files, aggregates the data, and saves it as a CSV file.
•	learning_model.py: Loads the aggregated data, preprocesses it, and trains a machine learning model to predict future prices.
•	main.py: Orchestrates the execution of the data fetching and processing scripts.

Installation

Prerequisites

•	Python 3.6 or newer
•	pip package manager

Dependencies

Install the required Python packages using the following command:
pip install -r requirements.txt

requirements.txt
requests
requests_cache
polars
scikit-learn

Setup

1. Clone Repo
git clone https://github.com/yourusername/runescape-price-prediction.git
cd runescape-price-prediction

2. Create necessary Dirrectories
mkdir output

Usage

Running the Data Collection and Processing Pipeline

Start the automated data fetching and processing by running the main.py script:
python main.py

•	Data Fetching: fetch_prices.py runs in a separate thread, fetching the latest prices every 5 minutes.
•	Data Processing: process_prices.py runs every 10 minutes to process and aggregate the fetched data.

Training the Machine Learning Model

After sufficient data has been collected and processed:
	1.	Ensure Data Availability
Confirm that aggregated_item_prices.csv exists in the output directory.
	2.	Update File Path in learning_model.py
Modify the file_path variable to point to the aggregated data:
file_path = 'output/aggregated_item_prices.csv'

3. Run the model training script
python learning_model.py

•	The script will load the data, preprocess it, and train two Random Forest models to predict high and low prices.
	•	It outputs the Mean Squared Error (MSE) and makes predictions on sample data.

Customization

•	Adjust Fetch Interval: Modify time.sleep(300) in fetch_prices.py to change the data fetching frequency.
•	Adjust Processing Interval: Change the time.sleep(600) in main.py to alter how often data is processed.
•	Experiment with Models: Edit learning_model.py to try different algorithms or hyperparameters.

Data Flow

1.	Fetching Data (fetch_prices.py)
  •	Connects to the RuneScape price API.
  •	Retrieves the latest prices and saves them as JSON files in output/.
2.	Processing Data (process_prices.py)
  •	Reads the JSON files from output/.
  •	Extracts and compiles price data into aggregated_item_prices.csv.
3.	Training Model (learning_model.py)
  •	Loads aggregated_item_prices.csv.
  •	Preprocesses data (handles nulls, selects features).
  •	Splits data into training and testing sets.
  •	Trains Random Forest models and evaluates performance.

API Information

•	Base URL: https://prices.runescape.wiki/api/v1/osrs
•	Endpoint Used: /latest for fetching the latest item prices.
•	Headers: Custom User-Agent header is set as per API guidelines.

Dependencies Breakdown

•	requests: For making HTTP requests to the API.
•	requests_cache: Caches API responses to minimize redundant requests.
•	polars: High-performance DataFrame library for data manipulation.
•	scikit-learn: Machine learning library used for model training and evaluation.

Troubleshooting

•	Connection Errors: Ensure you have a stable internet connection and the API is accessible.
•	Permission Issues: Verify that scripts have read/write permissions for the output directory.
•	Module Errors: Double-check that all dependencies are installed correctly.

Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

License

This project is licensed under the terms of the MIT license.

Acknowledgements

•	RuneScape API: Thanks to the RuneScape community for providing access to the price data API.
•	Open-Source Libraries: This project utilizes several open-source packages that greatly facilitated development.
