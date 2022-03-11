from tests.base_test import BaseTest
from pages.index.file_upload import FileUpload
from pages.utils.utils import Utils


class TestFileUpload(BaseTest):

    def setUp(self):
        super().setUp()
        self.file_upload = FileUpload(self.driver)
        self.driver.get(self.file_upload.base_url)
        self.utils = Utils(self.driver)

    def test_file_(self):
        self.file_upload.login()
        self.utils.admin_menu()
        self.assertIn("McKinsey Academy", self.driver.page_source)
        self.file_upload.add_resource_into_channel()
        expected_assert = self.utils.page_confirmation_title()
        self.assertEqual("Loading", expected_assert, "Comparison are not match")
        self.utils.pdf_file_upload()

    def tearDown(self):
        self.driver.quit()