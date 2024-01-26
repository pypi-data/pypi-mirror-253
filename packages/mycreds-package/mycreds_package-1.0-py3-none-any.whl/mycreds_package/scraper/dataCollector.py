# This function is called when already navigated to the course/section's Grading Sheet page.
# This function scrapes data from D1 and returns the Course Name, Completion Date, as well as the filtered list of students (name, email) who passed.


from selenium.webdriver.common.by import By
from .navClassList import navClassList

def dataCollector(driver):
    passIndexList = []
    stdNamesList = []
    stdEmailsList = []

    # Grabs course name
    course_name_element = driver.find_element(By.XPATH, '//span[@id="contextHeaderSpan"]')
    course_name = course_name_element.text.strip()[19:]

    # Grabs completion date in form DD MMM YYYY, DD is 0x if single digit date
    date_path = "//div[@class='title']/following::td[contains(@class, 'content') and contains(text(), 'Last Schedule Date:')]/following-sibling::td[@class='content']"
    date_element = driver.find_element(By.XPATH, date_path)
    completion_date = date_element.text.strip()

    # Find number of students in section
    number_of_student_element = driver.find_element(By.XPATH, '//*[@id="content01"]/form[1]/table[2]/tbody/tr[4]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]')
    number = int(number_of_student_element.text)
    page = 0

    # Creates list to keep track of indices of students to make certs for
    while True:
        for index in range(min(number, 50)):
            check_box_name = "listToBeRendered[{}].certificateReqsMet".format(index)
            check_box_element = driver.find_element(By.NAME, check_box_name)
            if check_box_element.is_selected():
                passIndexList.append(index + 50 * page)
        number = number - 50
        page = page + 1
        if number <= 0:
            break
        driver.find_element(By.CLASS_NAME, 'next').click()
    
    # Resets page and number
    while page != 0:
        number = number + 50
        page = page - 1

    # Navigate to Class List
    navClassList(driver)

    # Creates a list of all student emails
    while True:
        # Update list of student names
        name_elements = driver.find_elements(By.ID, 'studentName')
        stdNamesList = stdNamesList + [name_element.get_attribute('title') for name_element in name_elements]
        # Update list of student emails
        email_elements = driver.find_elements(By.ID, 'studentPreferredEmail')
        stdEmailsList = stdEmailsList + [email_element.get_attribute('title') for email_element in email_elements]
        
        number = number - 50
        page = page + 1
        if number <= 0:
            break
        driver.find_element(By.CLASS_NAME, 'next').click()

    # Combine lists of names and emails and filter according to indices list of passing students
    filtered_stds = [(stdNamesList[i], stdEmailsList[i]) for i in passIndexList]

    return {
        'course name': course_name,
        'completion date': completion_date,
        'students': filtered_stds,
    }