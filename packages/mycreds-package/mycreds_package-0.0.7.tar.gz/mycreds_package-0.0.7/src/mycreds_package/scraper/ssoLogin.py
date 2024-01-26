# This function performs WatSPEED SSO login given username and password

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def ssoLogin(driver, unInput, pwInput):
    # SSO ACC clear and input
    input_SSO_ACC = driver.find_element(By.ID, 'userNameInput')  
    input_SSO_ACC.clear()
    input_SSO_ACC.send_keys(unInput)
    # print("SSO ACC Input")

    driver.find_element(By.ID, 'nextButton').click()    

    # SSO PASS clar and input
    input_SSO_PASS = driver.find_element(By.ID, 'passwordInput')
    input_SSO_PASS.clear()
    input_SSO_PASS.send_keys(pwInput)
    # print("SSO PASS Input")

    driver.find_element(By.ID, 'submitButton').click()

    if driver.title != 'University of Waterloo- WatSPEED':
        print('Couldn\'t sign you in. Please ensure your credentials are correct.')
        driver.quit()
        sys.exit()
    else:
        print('Successfully signed you into ' + driver.title)