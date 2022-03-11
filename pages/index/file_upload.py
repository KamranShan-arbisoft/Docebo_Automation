import time
from pages.common.selector import FileUploadElement
from pages.index.login import LoginPage
from pages.utils.utils import Utils


class FileUpload(LoginPage):

    def add_resource_into_channel(self):
        # click on channels element into the admin menu
        Utils.element_to_be_clickable(self, FileUploadElement.input_search_channel)
        # Search the channel name into search box
        time.sleep(3)
        Utils.invisibility_of_element(self, FileUploadElement.channel_name)
        Utils.element_to_be_clickable(self, FileUploadElement.channel_name, '[DELETE] Data - SEPT20')
        # Click on search button
        Utils.element_to_be_clickable(self, FileUploadElement.search_btn)
        # Wait for the specific channel to appear on DOM and edit on that channel
        time.sleep(3)
        Utils.visibility_of_element_located(self, FileUploadElement.edit_channel_name)
        Utils.element_to_be_clickable(self, FileUploadElement.edit_channel_name)
        # Click on the content tab to upload pdf/image
        Utils.visibility_of_element_located(self, FileUploadElement.content_tab_elm)
        Utils.element_to_be_clickable(self, FileUploadElement.content_tab_elm)
        time.sleep(3)
        # First wait for the Asset element to appear in the DOM Than click on that element
        Utils.visibility_of_element_located(self, FileUploadElement.input_search_asset)
        Utils.element_to_be_clickable(self, FileUploadElement.asset_elm)