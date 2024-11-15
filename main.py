import threading
import time
import os
import subprocess


def run_fetch_prices():
    os.system('python fetch_prices.py')


def run_process_prices():
    subprocess.Popen(['python', 'process_prices.py'])

# fetch_prices script started in a separate thread
fetch_thread = threading.Thread(target=run_fetch_prices)
fetch_thread.start()

# Few second wait to ensure the fetching process starts
time.sleep(10)

# process_prices script runs periodically
while True:
    run_process_prices()
    time.sleep(600)  # should be 10 minutes?
