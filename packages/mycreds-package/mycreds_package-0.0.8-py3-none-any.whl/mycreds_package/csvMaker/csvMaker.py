# This function should take the scraped data, format it,
# and make the MyCredsCertificate.csv on the user's desktop.


import csv
import os
from .csvLists import csvLists

def csvMaker(scraped_data):
    csv_data = csvLists(scraped_data)

    # Get the path to the user's desktop directory
    desktop_path = os.path.expanduser("~/Desktop")

    # Specify the CSV file path on the user's desktop
    csv_file_path = os.path.join(desktop_path, "MyCredsCertificate.csv")

    # Open the CSV file in write mode
    with open(csv_file_path, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the data, including headers, to the CSV file
        writer.writerows(csv_data)