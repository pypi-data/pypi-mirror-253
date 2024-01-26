# Function reads csv and returns data in a dictionary

import os
import csv

def csvReader():
    # Lists to store data
    full_names = []
    course_names = []
    completion_dates = []

    # Specify the CSV file path on the user's desktop
    desktop_path = os.path.expanduser("~/Desktop")
    csv_file_path = os.path.join(desktop_path, "MyCredsCertificate.csv")


    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)    
        for row in csv_reader:
            # Extract data from each row
            full_name = row['fullName']
            course_name = row['Course Name']
            completion_date = row['Completion Date']
            
            # Append data to lists
            full_names.append(full_name)
            course_names.append(course_name)
            completion_dates.append(completion_date)
    
    return {
        'full names': full_names,
        'course names': course_names,
        'completion dates': completion_dates,
    }