
from pages.base_page import BasePage
import os
from pages.utils.utils import Utils
from pages.common.selector import LoginPageSelectors


class LoginPage(BasePage):

    def login(self):
        email = os.environ["EMAIL"]
        password = os.environ['PASSWORD']
        Utils.presence_of_element_located(self, LoginPageSelectors.name, email)
        Utils.presence_of_element_located(self, LoginPageSelectors.password, password)
        Utils.element_to_be_clickable(self, LoginPageSelectors.submit_btn)

