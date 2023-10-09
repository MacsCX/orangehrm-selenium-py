from selenium.webdriver.common.by import By

from common.base_objects import BaseObject, BasePage


class Locators:
    USERDROPDOWN = (By.CLASS_NAME, "oxd-userdropdown")
    USERDROPDOWN_NAME = (By.CLASS_NAME, "oxd-userdropdown-name")

    __sidepanel_option_xpath = lambda x: (
        By.XPATH,
        f'.//span[contains(@class, "oxd-main-menu-item--name") and text()="{x}"]',
    )

    SIDEPANEL_BODY = (By.CLASS_NAME, "oxd-sidepanel-body")
    SIDEPANEL_OPTION_ADMIN = __sidepanel_option_xpath("Admin")
    SIDEPANEL_OPTION_BUZZ = __sidepanel_option_xpath("Buzz")


class UserDropdown(BaseObject):
    def get_user_name_and_surname(self) -> str:
        return self.get_element(Locators.USERDROPDOWN_NAME).text


class SidePanel(BaseObject):
    def click_option_buzz(self):
        self.get_element(Locators.SIDEPANEL_OPTION_BUZZ).click()


class BaseLoggedPage(BasePage):
    @property
    def userdropdown(self) -> UserDropdown:
        return UserDropdown(self.driver)

    @property
    def sidepanel(self) -> SidePanel:
        return SidePanel(self.driver)


class DashboardPage(BaseLoggedPage):
    # TODO move this class to separate file under implementing dashboard-specific things
    pass
