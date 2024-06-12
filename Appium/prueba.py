import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US'
}

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        capabilities_options=UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()

if __name__ == '__main__':
    unittest.main()