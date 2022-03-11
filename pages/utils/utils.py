import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.selector import NewUSerSelectors
from pages.base_page import BasePage
from common.selector import FileUploadElement


class Utils(BasePage):

    def admin_menu(self):
        admin_menu_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, NewUSerSelectors.admin_menu))
        )
        admin_menu_button.click()

    def page_confirmation_title(self):
        confirmation_title = self.driver.title
        return confirmation_title

    def element_to_be_clickable(self, elm, keys=False):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elm)))
        element.click()
        if keys:
            element.click()
            element.send_keys(keys)

    def presence_of_element_located(self, elm, keys=False):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elm)))
        element.click()
        if keys:
            element.send_keys(keys)

    def visibility_of_element_located(self, elm):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elm)))

    def visibility_of_element_located_click(self, elm, keys=False):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elm)))
        element.click()
        if keys:
            element.send_keys(keys)

    def invisibility_of_element(self, elm):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elm)))

    def pdf_file_upload(self):
        pdf_file_path = '../common/dummy.pdf'
        png_file_path = '../common/dummy-image-jpg.png'
        pdf_path = os.path.abspath(pdf_file_path)
        png_path = os.path.abspath(png_file_path)

        wait = WebDriverWait(self.driver, 10)
        try:
            pdf_file = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, FileUploadElement.pdf_file_upload_element)))
            pdf_file.send_keys(pdf_path)
        except:
            image_file = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, FileUploadElement.imge_file_upload_element)))
            image_file.send_keys(png_path)
        # The reason for using time. sleep here is when we upload a file it will take some seconds. And then the
        # save button appears on DOM before full pdf/image file to uploads
        time.sleep(3)
        save_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, FileUploadElement.save_change_btn_element)))
        save_btn.click()