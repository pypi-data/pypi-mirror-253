# This function creates lists to be put into a csv file


from .nameFormatter import nameFormatter
from .dateFormatter import dateFormatter

def csvLists(scraped_data):
    # Set up csv headers
    csv_data = [
        ["id", "fullName", "email", "documentType", "display_name", "file", "initial_login_type", "initial_login_idp", "initial_login_value", "access_charge_method", "access_charge_amount", "access_charge_currency", "Course Name", "Completion Date", "Partner", "CSV File Name"]
    ]

    # Create list of lists containing data
    for (name, email) in scraped_data['students']:
        # Format name and date for csv
        formatted_name = nameFormatter(name)
        formatted_date = dateFormatter(scraped_data['completion date'])
        
        # Create row of data
        row = [
            "",                                 # [EMPTY] id
            formatted_name,                     # fullName
            email,                              # email
            "watspeed_course_certificate",      # documentType
            "WatSPEED Course Certificate",      # display_name
            formatted_name + ".pdf",            # file
            "email",                            # initial_login_type
            "",                                 # [EMPTY] Placeholder for initial_login_idp
            email,                              # initial_login_value
            "",                                 # [EMPTY] Placeholder for access_charge_method
            "",                                 # [EMPTY] Placeholder for access_charge_amount
            "",                                 # [EMPTY] Placeholder for access_charge_currency
            scraped_data['course name'],        # Course Name
            formatted_date,                     # Completion Date
            "",                                 # [EMPTY] Partner
            "MyCredsCertificate.csv"            # CSV File Name
        ]
        csv_data.append(row)

    return csv_data