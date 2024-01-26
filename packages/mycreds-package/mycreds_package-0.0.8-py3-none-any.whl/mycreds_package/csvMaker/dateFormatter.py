# This function takes a string of 'DD MMM YYYY' and produces a string of 'YYYY-MMM-DD'


from datetime import datetime

def dateFormatter(input_date):
    # Convert the input date string to a datetime object
    input_datetime = datetime.strptime(input_date, '%d %b %Y')

    # Extract year, month, and day components
    year = input_datetime.year
    month = input_datetime.strftime('%b').capitalize()  # Capitalize the first letter of the month
    day = input_datetime.strftime('%d')

    # Format the output date string as 'YYYY-MMM-DD'
    output_date = f"{year}-{month}-{day}"

    return output_date