from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.base_url = 'https://mckinseysandbox.docebosaas.com/learn'
        self.driver = driver