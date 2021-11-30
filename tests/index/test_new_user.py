import time

from tests.base_test import BaseTest
from pages.index.new_user import NewUser
from utils.utils import Utils


class TestNewUser(BaseTest):
    def setUp(self):
        super().setUp()
        self.new_user = NewUser(self.driver)
        self.driver.get(self.new_user.base_url)
        self.util = Utils(self.driver)

    def test_new_user(self):
        # Getting login() from parent BaseTest
        self.new_user.login()
        # Click to admin menu
        self.util.admin_menu()
        assert "McKinsey Academy" in self.driver.page_source
        # Click to new user button from admin menu
        self.new_user.new_user_buttons()
        # Adding new user general info
        self.new_user.fill_new_user_general_info()
        # waiting to the new branch screen and select all branch
        self.new_user.fill_new_user_branch_info()
        # Filling data into user additional fields
        self.new_user.fill_new_user_additional_info()
        # Click to Preview button
        self.new_user.preview_info_btn()
        # getting page title into "title_of_web_page" and use in assert
        assert "All Users - McKinsey Academy" in self.driver.page_source
        # Click to confirmation button
        self.new_user.what_next()
        # Again search the user in the search bar and make sure the user is added
        self.new_user.verify_user_added()

    def tearDown(self):
        self.driver.quit()