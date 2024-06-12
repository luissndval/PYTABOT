import time

from selenium.webdriver.common.by import By

from Appium.caps import desired_Caps
from Appium.data.Keycode import keycodes
from Appium.data.url import url
from Appium.elements.elements_Android import Elements
from _pom.Mobile.Mobile_Functions import MobileAutomation
from _pom.front.front import functions


class Mobile_device(MobileAutomation):

    def openMobile(self):
        capabilities = desired_Caps.capabilities
        appium_server_url = 'http://localhost:4723'
        time.sleep(5)
        MobileAutomation.init_driver(self, appium_server_url, capabilities)
        functions.click_Field(self,By.XPATH, Elements['T&C'])
        functions.click_Field(self,By.XPATH, Elements['No Thanks'])
        functions.click_Field(self, By.XPATH, Elements['Notify No Thanks'])
        time.sleep(5)

    def url_Text(self):
        link = url
        functions.input_Texto(self, By.XPATH, Elements['url_Bar'], link)
        MobileAutomation.send_keys(self, keycodes['Enter'])
        time.sleep(5)
        functions.screenShot(self, "Open Website")


