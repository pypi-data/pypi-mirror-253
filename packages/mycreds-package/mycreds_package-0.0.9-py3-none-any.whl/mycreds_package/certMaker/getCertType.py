# Prompt user for cert type


def getCertType(valid_inputs):
    while True:
        certType = input('Choose a cert type.\nType "bronze", "silver", or "gold" without the quotations: ').lower()

        if certType in valid_inputs:
            return certType
        else:
            print('Invalid input.')