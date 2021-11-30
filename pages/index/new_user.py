import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.fixtures.new_users_data import DICT
from common.selector import NewUSerSelectors
from pages.index.login import LoginPage


class NewUser(LoginPage):

    # Click on the user button from the admin menu then click on user branch and click on invisible new user button
    def new_user_buttons(self):
        click_to_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user))
        )
        click_to_user.click()

        time.sleep(3)
        click_to_new_user_branch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.new_user_branch))
        )
        click_to_new_user_branch.click()

        time.sleep(3)
        click_to_new_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.new_user))
        )
        click_to_new_user.click()

    # filling New user General Required information and some optional fields
    def fill_new_user_general_info(self):
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.user_name))
        )
        user_name.send_keys(DICT.user_data[0])

        email = self.driver.find_element_by_css_selector(NewUSerSelectors.user_email)
        email.send_keys(DICT.user_data[1])

        first_name = self.driver.find_element_by_css_selector(NewUSerSelectors.user_first_name)
        first_name.send_keys(DICT.user_data[2])

        last_name = self.driver.find_element_by_css_selector(NewUSerSelectors.user_last_name)
        last_name.send_keys(DICT.user_data[3])

        email_validation = self.driver.find_element_by_css_selector(NewUSerSelectors.email_validation_drop)
        email_validation.click()

        verified = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.email_validation_item))
        )
        verified.click()

        next_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.next_button)
        next_btn.click()

    # Add user into branches but it's an optional, not required field are there
    def fill_new_user_branch_info(self):
        branch_drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.all_branch))
        )
        branch_drop.click()

        branch_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.branch_item))
        )
        branch_item.click()

        next_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.next_button)
        next_btn.click()

    # Filling additional info form with some required fields "client Name, Client ID, Primary experience,"
    def fill_new_user_additional_info(self):
        client_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.client_name))
        )
        client_name.send_keys(DICT.user_data[4])

        client_id = self.driver.find_element_by_css_selector(NewUSerSelectors.client_id)
        client_id.send_keys(DICT.user_data[5])

        wave_cohort = self.driver.find_element_by_css_selector(NewUSerSelectors.wave_cohort)
        wave_cohort.send_keys(DICT.user_data[6])

        primary_experience = self.driver.find_element_by_css_selector(NewUSerSelectors.primary_experience_drop)
        primary_experience.click()

        # time.sleep(3)
        primary_experience_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.primary_experience_item))
        )
        primary_experience_item.click()

        group_work = self.driver.find_element_by_css_selector(NewUSerSelectors.group_work)
        group_work.send_keys(DICT.user_data[7])

        custom_field1 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field1)
        custom_field1.send_keys(DICT.user_data[8])

        custom_field2 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field2)
        custom_field2.send_keys(DICT.user_data[8])

        custom_field3 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field3)
        custom_field3.send_keys(DICT.user_data[8])

        custom_field4 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field4)
        custom_field4.send_keys(DICT.user_data[8])

        next_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.next_button)
        next_btn.click()

    # Before clicking on the new user button we are verifying New user information by clicking on Preview button..
    def preview_info_btn(self):
        preview_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.preview_btn))
        )
        preview_btn.click()

        create_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, NewUSerSelectors.create_user_button))
        )
        create_user.click()

    # After clicking on create new user button we will get the message "User successfully added" and Confirmation button
    def what_next(self):
        confirmation_bth = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.confirmation_btn))
        )
        confirmation_bth.click()

    # Again search the user in the search bar and make sure the user is added
    def verify_user_added(self):
        search_new_user = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.search_input))
        )
        search_new_user.click()
        search_new_user.send_keys(DICT.user_data[1])

        search_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.search_btn)
        search_btn.click()