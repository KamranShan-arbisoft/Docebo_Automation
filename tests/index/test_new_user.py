import time

from tests.base_test import BaseTest
from pages.index.new_user import NewUser


class TestNewUser(BaseTest):
    def setUp(self):
        super().setUp()
        self.new_user = NewUser(self.driver)
        self.driver.get(self.new_user.base_url)

    def test_new_user(self):
        # Getting login() from parent BaseTest
        self.new_user.login()
        # Click to admin menu
        self.new_user.admin_menu()
        # getting page title into "title_of_web_page" and use in assert
        title_of_web_page = self.driver.title
        assert title_of_web_page in self.driver.page_source
        # Click to new user button from admin menu
        self.new_user.new_user_buttons()
        # Adding new user general info
        self.new_user.fill_new_user_general_info()
        # waiting to the new branch screen and select all branch
        self.new_user.fill_new_user_branch_info()
        # Filling data into user additional fields
        self.new_user.fill_new_user_additional_info()
        # add team member as a manager
        self.new_user.preview()
        # getting page title into "title_of_web_page" and use in assert
        title_of_web_page = self.driver.title
        assert title_of_web_page in self.driver.page_source

    def tearDown(self):
        self.driver.quit()