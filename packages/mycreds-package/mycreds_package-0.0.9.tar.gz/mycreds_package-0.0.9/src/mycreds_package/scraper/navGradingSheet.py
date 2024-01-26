# This program navigates to the Grading Sheet page of the specified course/section from the D1 Landing Page


from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def navGradingSheet(driver, course_str, section_str):
    def submit_by_XPATH(driver, XPATH, content):
        input_box = driver.find_element(By.XPATH, XPATH)
        input_box.clear()
        input_box = driver.find_element(By.XPATH, XPATH)
        input_box.send_keys(content)

    def click_by_ID(driver, id):
        driver.find_element(By.ID, id).click()

    click_by_ID(driver, 'mainMenu')
    # print('Cur Button clicked')

    click_by_ID(driver, 'menu-link-CurrMgr')
    # print('Cur_CurrMgr Button clicked')

    submit_by_XPATH(driver, "//*[@id='courseSearch_courseNumber']", course_str)
    submit_by_XPATH(driver, "//*[@id='courseSearch_sectionNumber']", section_str)

    click_by_ID(driver, 'searchButton')
    # print('search Button clicked')

    click_by_ID(driver, 'course-{}-{}'.format(course_str, section_str))
    # print('Course Section clicked')

    ActionChains(driver).move_to_element(driver.find_element(By.ID, 'menu-link-CurrMgrCourses')).perform()
    # print('CurrMgrCourses hovered') 

    click_by_ID(driver, 'menu-link-CurrMgrCoursesCourseProfileGradingSheet')
    # print('Grading Sheet Button clicked') 