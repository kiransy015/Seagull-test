import json
import unittest
import time
from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.util import create_driver


class TestloginU15678(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()


    def test_valid_login_TC156826(self):
        data = json.load(open('./test/regression/login/test-data/U15678.json'))

        self.login.wait_for_login_page_to_load()
        time.sleep(10)
        self.login.get_username_textbox().send_keys(data['TC156826']['UN'])
        self.login.get_password_textbox().send_keys(data['TC156826']['PWD'])
        self.login.get_login_buton().click()

        #Verify Home Page
        self.home.wait_for_home_page_to_load()
        print("Actual title :",self.driver.title)
        actual_title = self.driver.title
        expected_title = data['TC156826']['title']
        assert actual_title==expected_title

        #Logout from application
        self.home.get_logout_button().click()

        #Verify the LoginPage
        self.login.wait_for_login_page_to_load()


