from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.selector import NewUSerSelectors
from pages.base_page import BasePage


class Utils(BasePage):

    def admin_menu(self):
        admin_menu_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.admin_menu))
        )
        admin_menu_button.click()


