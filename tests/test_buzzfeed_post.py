import pytest

from common.base_objects import prepare_logger
from common.pages.base_logged_page import DashboardPage
from common.pages.buzz_page import BuzzPage
from common.test_utils.base_test_class import BaseTestClass
from common.test_utils.test_data import BuzzPostsData
from datetime import datetime
from time import sleep

logger = prepare_logger()


@pytest.mark.happy
@pytest.mark.buzz
@pytest.mark.parametrize("text", [BuzzPostsData.TREE, BuzzPostsData.XIAOMI, BuzzPostsData.SULTAN])
class TestBuzzPosting(BaseTestClass):
    """
    2. Scenario 2
    a. Navigate to the test site
    b. Capture the Username and Password mentioned in the test screen
    c. Use them and log in
    d. Validate that upon successful login, you are able to see the logged in user (displayed
    at top right corner)
    e. Print the Name of the user in the report

    additional points:
    f. Go to Buzz page
    h. Write a new post
    i. Validate if it's shown properly
    """

    def test_001_writing_posts(self, text: str):
        logger.info("TC001 - Write Buzz post and check if it's shown")
        page = DashboardPage(self.driver)

        user_data_from_dropdown = page.userdropdown.get_user_name_and_surname()
        logger.warning(f"User data: {user_data_from_dropdown}")

        page.sidepanel.click_option_buzz()

        page = BuzzPage(self.driver)
        page.wait_for_page_loaded()

        page.write_new_post(text)
        datetime_of_posting = int(datetime.now().timestamp() / 1000)

        sleep(2)
        post = page.get_newest_post_details()

        issues = page.check_for_issues_for_post(
            post_details=post, expected_content=text, expected_datetime=datetime_of_posting, expected_author=user_data_from_dropdown
        )

        if issues:
            raise AssertionError(f"Found issues: {';'.join(issues)}")
        else:
            assert True
