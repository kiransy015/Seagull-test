from lib.util import timeout_handlers

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        element = self.driver.find_element_by_id('container')
        timeout_handlers.wait_for_element_visibility(self.driver,element)

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_xpath("//a[@id='logoutLink']")
        except:
            return None

