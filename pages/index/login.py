import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.selector import LoginPageSelectors
from pages.base_page import BasePage

import os


class LoginPage(BasePage):

    def login(self):
        user_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageSelectors.name))
        )
        user_name.click()
        email = os.environ["EMAIL"]
        user_name.send_keys(email)

        user_pwd = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageSelectors.password))
        )
        user_pwd.click()
        password = os.environ['PASSWORD']
        user_pwd.send_keys(password)

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageSelectors.submit_btn))
        )
        submit_button.click()
