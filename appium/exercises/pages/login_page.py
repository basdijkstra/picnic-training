from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, appium_driver):
        super().__init__(appium_driver)
        self._username = (AppiumBy.ACCESSIBILITY_ID, 'Username input field')
        self._password = (AppiumBy.ACCESSIBILITY_ID, 'Password input field')
        self._login_button = (AppiumBy.ACCESSIBILITY_ID, 'Login button')

    def login_as(self, username, password):
        self.send_keys(self._username, username)
        self.send_keys(self._password, password)
        self.click(self._login_button)
