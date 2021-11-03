import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from comman.fixtures.new_users_data import DICT
from comman.selector import NewUSerSelectors
from pages.index.login import LoginPage


class NewUser(LoginPage):
    def admin_menu(self):
        admin_menu_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.admin_menu))
        )
        admin_menu_button.click()

    def new_user_buttons(self):
        click_to_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user))
        )
        click_to_user.click()

        time.sleep(3)
        click_to_new_user = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.new_user))
        )
        click_to_new_user.click()

        time.sleep(3)
        click_to_visible_new_user = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.visible_new_user))
        )
        click_to_visible_new_user.click()

    def fill_new_user_general_info(self):
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user_name))
        )
        user_name.click()
        user_name.send_keys(DICT.user_data[0])

        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user_email))
        )
        email.click()
        email.send_keys(DICT.user_data[1])

        first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user_first_name))
        )
        first_name.click()
        first_name.send_keys(DICT.user_data[2])

        last_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user_last_name))
        )
        last_name.click()
        last_name.send_keys(DICT.user_data[3])

        email_validation = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.email_validation_drop))
        )
        email_validation.click()

        verified = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.email_validation_item))
        )
        verified.click()

        next_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.next_button))
        )
        next_btn.click()

    def fill_new_user_branch_info(self):
        branch_drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.all_branch))
        )
        branch_drop.click()

        branch_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.branch_item))
        )
        branch_item.click()

        next_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.next_button))
        )
        next_btn.click()

    def fill_new_user_additional_info(self):
        client_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.client_name))
        )
        client_name.click()
        client_name.send_keys(DICT.user_data[4])

        client_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.client_id))
        )
        client_id.click()
        client_id.send_keys(DICT.user_data[5])

        wave_cohort = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.wave_cohort))
        )
        wave_cohort.click()
        wave_cohort.send_keys(DICT.user_data[6])

        primary_experience = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.primary_experience_drop))
        )
        primary_experience.click()

        # time.sleep(3)
        primary_experience_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.primary_experience_item))
        )
        primary_experience_item.click()

        group_work = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.group_work))
        )
        group_work.click()
        group_work.send_keys(DICT.user_data[7])

        custom_field1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.custom_field1))
        )
        custom_field1.click()
        custom_field1.send_keys(DICT.user_data[8])

        custom_field2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.custom_field2))
        )
        custom_field2.click()
        custom_field2.send_keys(DICT.user_data[8])

        custom_field3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.custom_field3))
        )
        custom_field3.click()
        custom_field3.send_keys(DICT.user_data[8])

        custom_field4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.custom_field4))
        )
        custom_field4.click()
        custom_field4.send_keys(DICT.user_data[8])

        next_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.next_button))
        )
        next_btn.click()

    def preview(self):
        preview_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.preview_btn))
        )
        preview_btn.click()

        create_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.create_user_button))
        )
        create_user.click()

    def verify_user_added(self):
        search_new_user = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.search_input))
        )
        search_new_user.click()
        search_new_user.send_keys(DICT.user_data[1])

        search_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.search_btn))
        )
        search_btn.click()