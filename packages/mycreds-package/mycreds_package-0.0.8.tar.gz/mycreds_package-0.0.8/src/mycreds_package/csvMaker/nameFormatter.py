# This function formats names to input in the csv


import re

def nameFormatter(name):
    # Split the name into last name and first name
    last_name, first_name = map(str.strip, name.split(','))

    # Capitalize each word in the first and last name
    last_name = re.sub(r'\b\w', lambda match: match.group().capitalize(), last_name)
    first_name = re.sub(r'\b\w', lambda match: match.group().capitalize(), first_name)

    # Format the name as 'firstName lastName'
    formatted_name = f"{first_name} {last_name}"

    return formatted_name