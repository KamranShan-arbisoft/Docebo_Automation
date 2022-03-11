import time
from pages.index.login import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def setUp(self):
        super().setUp()
        time.sleep(5)
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.login_page.base_url)

    def test_login_page(self):
        self.login_page.login()
        title_of_web_page = self.driver.title
        assert title_of_web_page in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

