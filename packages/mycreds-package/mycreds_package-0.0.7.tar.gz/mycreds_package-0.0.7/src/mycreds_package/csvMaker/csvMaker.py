# This function should take the scraped data, format it,
# and make the MyCredsCertificate.csv in the parent directory.


import csv
import os
from .csvLists import csvLists

def csvMaker(scraped_data):
    csv_data = csvLists(scraped_data)

    # Specify the CSV file path in the parent directory
    csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "MyCredsCertificate.csv")

    # Open the CSV file in write mode
    with open(csv_file_path, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the data, including headers, to the CSV file
        writer.writerows(csv_data)