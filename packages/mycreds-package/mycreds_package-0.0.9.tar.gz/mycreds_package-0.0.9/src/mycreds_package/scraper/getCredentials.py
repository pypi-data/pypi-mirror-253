# This function prompts the user for username and password


import getpass

def getCredentials():
    while True:
        username = input("Enter your @uwaterloo account: ")
        if username.endswith("@uwaterloo.ca"):
            break
        else:
            print("Invalid username. Please enter a valid @uwaterloo.ca account.")
    
    password = getpass.getpass("Enter your password: ")

    return username, password