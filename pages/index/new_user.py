import time
from pages.common.selector import NewUSerSelectors
from pages.utils.utils import Utils
from pages.index.login import LoginPage
from pages.index import config


class NewUser(LoginPage):

    # Click on the user button from the admin menu then click on user branch and click on invisible new user button
    def new_user_buttons(self):
        Utils.presence_of_element_located(self, NewUSerSelectors.user)
        time.sleep(3)
        Utils.presence_of_element_located(self, NewUSerSelectors.new_user_branch)
        time.sleep(3)
        Utils.element_to_be_clickable(self, NewUSerSelectors.new_user)

    # filling New user General Required information and some optional fields
    def fill_new_user_general_info(self):
        Utils.presence_of_element_located(self, NewUSerSelectors.user_name, config.user_name)

        email = self.driver.find_element_by_css_selector(NewUSerSelectors.user_email)
        email.send_keys(config.email)

        first_name = self.driver.find_element_by_css_selector(NewUSerSelectors.user_first_name)
        first_name.send_keys(config.first_name)

        last_name = self.driver.find_element_by_css_selector(NewUSerSelectors.user_last_name)
        last_name.send_keys(config.last_name)

        email_validation = self.driver.find_element_by_css_selector(NewUSerSelectors.email_validation_drop)
        email_validation.click()

        Utils.element_to_be_clickable(self, NewUSerSelectors.email_validation_item)

        next_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.next_button)
        next_btn.click()

    # Add user into branches but it's an optional, not required field are there
    def fill_new_user_branch_info(self):
        Utils.visibility_of_element_located_click(self, NewUSerSelectors.all_branch)

        Utils.visibility_of_element_located_click(self, NewUSerSelectors.branch_item)

        next_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.next_button)
        next_btn.click()

    # Filling additional info form with some required fields "client Name, Client ID, Primary experience,"
    def fill_new_user_additional_info(self):
        Utils.presence_of_element_located(self, NewUSerSelectors.client_name, config.client_name)

        client_id = self.driver.find_element_by_css_selector(NewUSerSelectors.client_id)
        client_id.send_keys(config.client_id)

        wave_cohort = self.driver.find_element_by_css_selector(NewUSerSelectors.wave_cohort)
        wave_cohort.send_keys(config.wave_cohort)

        primary_experience = self.driver.find_element_by_css_selector(NewUSerSelectors.primary_experience_drop)
        primary_experience.click()

        Utils.element_to_be_clickable(self, NewUSerSelectors.primary_experience_item)

        group_work = self.driver.find_element_by_css_selector(NewUSerSelectors.group_work)
        group_work.send_keys(config.group_work)

        custom_field1 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field1)
        custom_field1.send_keys(config.custom_field1)

        custom_field2 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field2)
        custom_field2.send_keys(config.custom_field1)

        custom_field3 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field3)
        custom_field3.send_keys(config.custom_field1)

        custom_field4 = self.driver.find_element_by_css_selector(NewUSerSelectors.custom_field4)
        custom_field4.send_keys(config.custom_field1)

        next_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.next_button)
        next_btn.click()

    # Before clicking on the new user button we are verifying New user information by clicking on Preview button..
    def preview_info_btn(self):
        Utils.presence_of_element_located(self, NewUSerSelectors.preview_btn)

        Utils.element_to_be_clickable(self, NewUSerSelectors.create_user_button)

    # After clicking on create new user button we will get the message "User successfully added" and Confirmation button
    def what_next(self):
        Utils.visibility_of_element_located(self, NewUSerSelectors.confirmation_btn)
        Utils.presence_of_element_located(self, NewUSerSelectors.confirmation_btn)

    # Again search the user in the search bar and make sure the user is added
    def verify_user_added(self):
        Utils.visibility_of_element_located_click(self, NewUSerSelectors.search_input, config.email)
        search_btn = self.driver.find_element_by_css_selector(NewUSerSelectors.search_btn)
        search_btn.click()
