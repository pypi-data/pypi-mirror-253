# MAIN SCRIPT
# To run, enter in terminal:
#   python MyCreds.py


import sys
from os import path

# Set the package name to the current directory (package)
__package__ = path.basename(path.dirname(path.abspath(__file__)))

# Add the current directory to sys.path
sys.path.append(path.abspath(path.dirname(__file__)))

from scraper.scraper import scraper
from csvMaker.csvMaker import csvMaker
from certMaker.certMaker import certMaker

def main():
    scraped_data = scraper()
    print('Web-scraping completed successfully.')
    print('Scraped Data:')
    print(scraped_data)

    csvMaker(scraped_data)
    print('CSV creation completed successfully.')

    certMaker()
    print('Program executed successfully. Check the newBatch folder for your PDF certificates. Have a nice day! :D')

main()