import threading
import time
import os


def run_fetch_prices():
    os.system('python fetch_prices.py')


def run_process_prices():
    os.system('python process_prices.py')

# Start the fetch_prices script in a separate thread
fetch_thread = threading.Thread(target=run_fetch_prices)
fetch_thread.start()

# Wait a few seconds to ensure the fetching process starts
time.sleep(10)

# Run the process_prices script periodically (e.g., every 10 minutes)
while True:
    run_process_prices()
    time.sleep(600)  # 10 minutes
