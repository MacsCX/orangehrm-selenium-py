import pytest
from selenium import webdriver

import common.test_utils.test_data as TD
from common.base_objects import prepare_logger
from common.pages.login_page import LoginPage
from common.test_utils.base_test_class import BaseTestClass

logger = prepare_logger()


"""
1. Scenario 1
a. Navigate to the test site in a browser
b. Try to login with any random username and password
c. Validate that the Invalid Credentials message is correctly displayed
"""


@pytest.mark.unhappy
@pytest.mark.login
class TestFailedLogin(BaseTestClass):
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TD.TEST_ENV_MAIN_URL)

    @pytest.mark.parametrize("username,password", TD.LoginData.WRONG_CREDENTIALS_DATA_SET)
    def test_001_incorrect_login(self, username, password):
        logger.info("TC001 - Check failed login with wrong credentials")
        page = LoginPage(self.driver)

        page.input_credentials(username, password)
        page.click_login()

        assert page.is_invalid_credentials_alert_visible()

    @pytest.mark.parametrize("username,password", TD.LoginData.MISSING_CREDENTIALS_DATA_SET)
    def test_missing_creds_login(self, username, password):
        logger.info("TC002 - Check failed login with missing credentials")
        page = LoginPage(self.driver)

        page.input_credentials(username, password)
        page.click_login()

        issues = page.check_for_issues_for_required_error_visibility(username, password)

        if issues:
            raise AssertionError(f"Found issues: {';'.join(issues)}")
        else:
            assert True
