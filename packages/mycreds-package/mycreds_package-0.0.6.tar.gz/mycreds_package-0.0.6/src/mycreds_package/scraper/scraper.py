# This scraper performs the following functions:
#   - Retrieves a course and section number
#   - Retrieves user WatIAM credentials and completes SSO login
#   - Accesses D1 prod/test env
#   - Navigate to specified course and section number's Grading Sheet page
#   - Scrapes Course Name and Completion Date
#   - Tracks list of students who passed (by index)
#   - Navigates to class list
#   - Creates a list of tuples (student name, student email)
#   - Filters list of tuples to only students who passed
#   - Returns a dictionary of:
#       'course name': course_name,
#       'completion date': completion_date,
#       'students': filtered_stds,
#
#   USE 0013 - 004 Digital Transformation AS A TESTER FOR THE PROD ENVIRONMENT
#   USE 0013 - 002 Digital Transformation AS A TESTER FOR THE TEST ENVIRONMENT
#   USE 0047 - 005 IN TEST ENV FOR BIIIIIIG SECTION


from selenium import webdriver
from selenium.webdriver.common.by import By
from .getCourseSec import getCourseSec
from .getCredentials import getCredentials
from .ssoLogin import ssoLogin
from .navGradingSheet import navGradingSheet
from .dataCollector import dataCollector

def scraper():
    # Get course and section number
    course_str, section_str = getCourseSec()

    # Get user WatSPEED credentials
    (unInput, pwInput) = getCredentials()

    # Use Chrome Web Browser
    driver = webdriver.Chrome()
    # Set global wait time to 10 seconds-- if program can't find element in 10 seconds, shuts down
    driver.implicitly_wait(10)

    # Navigate to test/prod environment
    # driver.get('https://uofwaterlootestsv.destinyone.moderncampus.net/')  # D1 test site
    driver.get('https://uofwaterloosv.destinyone.moderncampus.net/')        # D1 prod site

    # Login to WatSPEED SSO using user-provided credentials
    ssoLogin(driver, unInput, pwInput)

    # Navigate to the Grading Sheet
    navGradingSheet(driver, course_str, section_str)

    # Collect data
    scraped_data = dataCollector(driver)
    
    print('Processing data, please wait a moment...')

    # Close the browser
    driver.quit()
    
    return scraped_data