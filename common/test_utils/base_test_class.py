from selenium import webdriver

from common.pages.login_page import LoginPage
from common.test_utils.test_data import TEST_ENV_MAIN_URL


class BaseTestClass:
    driver = None

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TEST_ENV_MAIN_URL)

        page = LoginPage(self.driver)

        username = page.get_test_data_username()
        password = page.get_test_data_password()
        page.input_credentials(username, password)
        page.click_login()

    def teardown_method(self):
        self.driver.quit()
