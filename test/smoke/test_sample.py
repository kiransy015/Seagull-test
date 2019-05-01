import unittest
import json
import time
from lib.ui.login_page import LoginPage
from lib.util import create_driver,timeout_handlers

class TestSample(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_Sample(self):
        test_data = json.load(open('./test/smoke/test-data/Sample_data.json'))
        self.login.wait_for_login_page_to_load()
        timeout_handlers.wait_for_title_of_webpage(self.driver,test_data['title'])
        actual_title = self.driver.title
        print("Actual title :",actual_title)
        assert actual_title==test_data['title']