import logging
from time import sleep
from typing import Callable, Iterable

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def prepare_logger() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
    )
    return logging.getLogger(__name__)


log = prepare_logger()


class Locators:
    LOADING_SPINNER = (By.XPATH, './/div[contains(@class, "loading-spinner")]')


class BaseObject:
    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver

    def get_element(
        self,
        locator: tuple,
        timeout_sec: int = 5,
        expected_condition: EC = EC.presence_of_element_located,
    ) -> WebElement:
        log.info(f"Trying to find element: {locator}")
        return WebDriverWait(self.driver, timeout_sec).until(expected_condition(locator))

    def get_elements(self, locator: tuple, timeout_sec: int = 10) -> Iterable[WebElement]:
        log.info(f"Trying to find elements: {locator}")
        WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_element_located(locator))

        return self.driver.find_elements(*locator)

    def is_element_visible(self, locator: tuple, element: WebElement = None, *args, **kwargs) -> bool:
        try:
            element = self.__handle_locator_or_element(locator=locator, element=element, *args, **kwargs)
            return element.is_displayed()
        except TimeoutException:
            return False

    def __handle_locator_or_element(self, locator: tuple = None, element: WebElement = None, *args, **kwargs) -> WebElement:
        """
        In WebElement-related methods I implemented two different params: locator and element,
        because I would like to give a choice to a test framework user
        :param locator:
        :param element:
        :return: WebElement
        """

        if locator is None and element is None:
            raise ValueError("You must pass one param to this method: locator or element!")

        if element is not None:
            return element

        if locator is not None:
            return self.get_element(locator=locator, *args, **kwargs)


class BasePage(BaseObject):
    title = ""
    endpoint = ""

    def __init__(self, driver: RemoteWebDriver, *args, **kwargs):
        super().__init__(driver=driver, *args, **kwargs)

    def scroll_to_top(self):
        sleep(0.5)
        self.driver.execute_script("window.scrollTo(0, 0)")
        sleep(0.5)

    def wait_for_page_loaded(self):
        WebDriverWait(self.driver, 5).until(EC.staleness_of(self.get_element(Locators.LOADING_SPINNER)))
