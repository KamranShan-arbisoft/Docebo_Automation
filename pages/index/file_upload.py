import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.selector import FileUploadElement
from pages.index.login import LoginPage


class FileUpload(LoginPage):

    file_path = '/Users/hafizkamran/Documents/Docebo_Automation/common/dummy.pdf'
    abs_path = os.path.abspath(file_path)

    def pdf_file_upload(self):

        # Direct navigate to the exact location where i can upload the file
        self.driver.get('https://mckinseysandbox.docebosaas.com/share/asset/edit/385')
        file_upload = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, FileUploadElement.file_upload_element))
        )
        file_upload.send_keys(self.abs_path)
        time.sleep(3)
        save_change_btn = self.driver.find_element_by_css_selector(FileUploadElement.save_change_btn_element)
        save_change_btn.click()


