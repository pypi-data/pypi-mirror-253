# This program navigates to the Class List page from a Grading Sheet page


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def navClassList(driver):
    ActionChains(driver).move_to_element(driver.find_element(By.ID, 'menu-link-CurrMgrCourses')).perform()
    # print('CurrMgrCourses hovered') 

    driver.find_element(By.ID, 'menu-link-CurrMgrCoursesCourseProfileClassList').click()
    # print('Class List Button clicked')

    # Include all students
    dropdown_element = driver.find_element(By.NAME, 'selectedRoleFilter')
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text('Completion Status: All')

    # Uncheck Omit withdrawn students checkbox if checked
    checkbox_element = driver.find_element(By.XPATH, "//input[@name='omitWithdrawnStudents']")
    if checkbox_element.is_selected():
        checkbox_element.click()
    
    driver.find_element(By.XPATH, '//button[@value="Go"]').click()