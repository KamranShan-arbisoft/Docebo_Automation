import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    __driver = None # why we are using

    @classmethod
    def setUpClass(cls):
        cls.__driver = webdriver.Chrome('/Users/hafizkamran/Documents/edx-selenium-project/tests/chromedriver')
        # cls.__driver.implicitly_wait(5)

    @property
    def driver(self):
        return self.__driver

    # @classmethod
    # def tearDownClass(cls):
    #     cls.__driver.quit()

