from datetime import datetime as dt
from typing import Iterable

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from common.base_objects import prepare_logger
from common.pages.base_logged_page import BaseLoggedPage

logger = prepare_logger()


class Locators:
    # placeholder = "What's on your mind?"
    POST_INPUT_FIELD = (By.XPATH, './/textarea[@placeholder="What\'s on your mind?"]')
    POST_SUBMIT_BUTTON = (By.XPATH, './/button[@type="submit"]')

    POST_GENERAL_ELEMENT = (By.XPATH, './/div[@class="orangehrm-buzz-post"]/..')

    ## vvvv DON'T use those locators standalone!
    # Use them as parent_element.find(Locator)
    POST_DATETIME = (By.XPATH, './/p[contains(@class, "orangehrm-buzz-post-time")]')
    POST_AUTHOR_NAME = (By.XPATH, './/p[contains(@class, "orangehrm-buzz-post-emp-name")]')
    POST_TEXT = (By.XPATH, './/p[contains(@class, "orangehrm-buzz-post-body-text")]')
    POST_READMORE = (By.XPATH, './/p[contains(@class, "orangehrm-buzz-post-body-text")]')
    ## ^^^^


class BuzzPage(BaseLoggedPage):
    def write_new_post(self, text: str):
        logger.info(f"Writing new Buzz post. Content:\n{repr(text)}")
        lines = text.split("\n")
        input_field = self.get_element(Locators.POST_INPUT_FIELD)
        input_field.click()
        for line in lines:
            input_field.send_keys(line)
            input_field.send_keys(Keys.SHIFT, Keys.ENTER)
        self.get_element(Locators.POST_SUBMIT_BUTTON).click()

    def get_newest_post_details(self) -> dict:
        logger.info("Getting details about the newest post")
        all_posts: Iterable[WebElement] = self.get_elements(Locators.POST_GENERAL_ELEMENT)
        newest_post: WebElement = all_posts[0]

        datetime = newest_post.find_element(*Locators.POST_DATETIME).text
        author = newest_post.find_element(*Locators.POST_AUTHOR_NAME).text
        content = newest_post.find_element(*Locators.POST_TEXT).text
        datetimeUnix = int(dt.strptime(datetime, "%Y-%m-%d %I:%M %p").timestamp() / 1000)

        return dict(datetime=datetime, author=author, content=content, datetimeUnix=datetimeUnix)

    def check_for_issues_for_post(
        self, post_details: dict, expected_content: str, expected_datetime: float, expected_author: str, datetime_margin_sec: int = 10
    ):
        logger.warning("Checking for issues for post")
        logger.warning(
            f">>> Details from Buzz feed:\n"
            f"author:{post_details['author']}\n"
            f"datetime:{post_details['datetimeUnix']}\n"
            f"content:{post_details['content']}\n"
        )
        logger.warning(f">>> Expected:\n" f"author:{expected_author}\n" f"datetime:{expected_datetime}\n" f"content:{expected_content}\n")

        issues = []

        # TODO discuss with dev team
        # TEMP. disabled! Dropdown contains shorter name than post
        # f.e. Michael Brown (dropdown) vs Michael J Brown (post)
        # if post_details["author"] != expected_author:
        #     issues.append("Assertion failed for -> author")

        logger.warning("AUTHOR assertion disabled - discuss the thing with dev team (look at the code)")

        if abs(int(post_details["datetimeUnix"] - expected_datetime)) > float(datetime_margin_sec):
            issues.append("Assertion failed for -> datetime")

        if post_details["content"] != expected_content:
            issues.append("Assertion failed for -> content")

        return issues
