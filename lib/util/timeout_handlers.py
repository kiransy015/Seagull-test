from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def wait_for_element_visibility(driver,element):
    wait = WebDriverWait(driver,60)
    wait.until(expected_conditions.visibility_of(element))

def wait_for_title_of_webpage(driver,title):
    wait = WebDriverWait(driver, 60)
    wait.until(expected_conditions.title_contains(title))

def wait_for_alert_popup(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(expected_conditions.alert_is_present())