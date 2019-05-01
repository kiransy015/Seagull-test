from lib.util import timeout_handlers

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        element = self.driver.find_element_by_name('username')
        timeout_handlers.wait_for_element_visibility(self.driver,element)

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_name('username')
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name('pwd')
        except:
            return None

    def get_login_buton(self):
        try:
            return self.driver.find_element_by_xpath("//a[@id='loginButton']//div[contains(text(),'Login')]")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Username or Password is invalid. Please try again.']")
        except:
            return None