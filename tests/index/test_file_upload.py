import time

from tests.base_test import BaseTest
from pages.index.file_upload import FileUpload


class TestFileUpload(BaseTest):

    def setUp(self):
        super().setUp()
        self.file_upload = FileUpload(self.driver)
        self.driver.get(self.file_upload.base_url)

    def test_file_(self):
        self.file_upload.login()
        time.sleep(3)
        self.file_upload.pdf_file_upload()

    def tearDown(self):
        self.driver.quit()