import pytest
from selenium.webdriver import Chrome,Firefox,Ie

def get_browser_instance():
    browser_info=pytest.config.option.browser
    test_url_info=pytest.config.option.url
    if browser_info.lower()=='chrome':
        driver = Chrome('./browser-servers/chromedriver.exe')
    elif browser_info.lower()=='firefox':
        driver = Chrome('./browser-servers/geckodriver.exe')
    elif browser_info.lower()=='ie':
        driver = Chrome('./browser-servers/iedriver.exe')
    else:
        print('!!!Invalid Browser option please check ---browser parameter from CMD!!!')

    driver.maximize_window()
    driver.implicitly_wait(30)
    if test_url_info.lower()=='test':
        driver.get('https://demo.actitime.com/login.do')
    elif test_url_info.lower()=='prod':
        driver.get('https://demo.actitime.com/login.do')
    return driver