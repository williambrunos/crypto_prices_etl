import requests
from datetime import datetime
import csv
import os
import pprint
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

    
def main():
    logger.info(f'Requesting assets data from coinmarketcap API')
    run_id = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    url = 'https://api.coincap.io/v2/assets'

    raw_data = requests.get(url).json().get('data', [])
    
    logger.info(f'Loading data extracted from the API into a csv file')
    raw_output_file = f'./data/{run_id}.csv'
    fields_names = list(raw_data[0].keys())
    
    logger.info(f'Writing data to {raw_output_file}')
    with open(raw_output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields_names)
        writer.writeheader()
        
        for d in raw_data:
            writer.writerow(d)
        
    logger.info('Job finished')
    

if __name__ == '__main__':
    main()