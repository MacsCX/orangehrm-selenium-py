from selenium.webdriver.common.by import By

from common.base_objects import BasePage


class Locators:
    TEST_DATA_BOX_USERNAME = (
        By.XPATH,
        './/div[contains(@class, "orangehrm-demo-credentials")]/*[1]',
    )
    TEST_DATA_BOX_PASSWORD = (
        By.XPATH,
        './/div[contains(@class, "orangehrm-demo-credentials")]/*[2]',
    )

    USERNAME_INPUT = (By.XPATH, './/input[@name="username"]')
    PASSWORD_INPUT = (By.XPATH, './/input[@name="password"]')

    # TODO ask devs for better selectors!
    # using movements from child to parents can be unstable DOM will change
    USERNAME_REQUIRED_ERROR = (
        By.XPATH,
        './/input[@name="username"]/../../span[text()="Required"]',
    )
    PASSWORD_REQUIRED_ERROR = (
        By.XPATH,
        './/input[@name="password"]/../../span[text()="Required"]',
    )

    LOGIN_BUTTON = (By.XPATH, './/button[@type="submit"]')

    INVALID_CREDS_BOX_ALERT = (
        By.XPATH,
        './/div[@role="alert"]//p[text()="Invalid credentials"]',
    )


class LoginPage(BasePage):
    def get_test_data_username(self) -> str:
        return self.get_element(Locators.TEST_DATA_BOX_USERNAME).text.replace("Username : ", "")

    def get_test_data_password(self) -> str:
        return self.get_element(Locators.TEST_DATA_BOX_PASSWORD).text.replace("Password : ", "")

    def input_username(self, username: str):
        self.get_element(Locators.USERNAME_INPUT).send_keys(username)

    def input_password(self, password: str):
        self.get_element(Locators.PASSWORD_INPUT).send_keys(password)

    def input_credentials(self, username: str, password: str):
        self.get_element(Locators.USERNAME_INPUT).send_keys(username)
        self.get_element(Locators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.get_element(Locators.LOGIN_BUTTON).click()

    def is_invalid_credentials_alert_visible(self) -> bool:
        return self.is_element_visible(Locators.INVALID_CREDS_BOX_ALERT)

    def is_username_required_error_visible(self) -> bool:
        return self.is_element_visible(Locators.USERNAME_REQUIRED_ERROR)

    def is_password_required_error_visible(self) -> bool:
        return self.is_element_visible(Locators.PASSWORD_REQUIRED_ERROR)

    def check_for_issues_for_required_error_visibility(self, username: str, password: str) -> list:
        issues = []
        username_error_visible = self.is_username_required_error_visible()
        password_error_visible = self.is_password_required_error_visible()

        if not username and not username_error_visible:
            issues.append("`Required` error for username IS NOT visible!")

        if username and username_error_visible:
            issues.append("`Required` error for username IS visible!")

        if not password and not password_error_visible:
            issues.append("`Required` error for password IS NOT visible!")

        if password and password_error_visible:
            issues.append("`Required` error for password IS visible!")

        return issues
