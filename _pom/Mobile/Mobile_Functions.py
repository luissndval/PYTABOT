import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MobileAutomation():
    def __init__(self):
        #self.config = config
        self.driver = None

    def init_driver(self,appium_server_url,capabilities):
        #capabilities_options=UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def quit_driver(self):
        # Cerrar el driver de Appium.
        if self.driver is not None:
            self.driver.quit()

    def find_element(self, locator_type, locator_value):
        # Método para encontrar un elemento con espera explícita.
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )

    def click(self, locator_type, locator_value):
        # Método para hacer clic en un elemento.
        element = self.find_element(locator_type, locator_value)
        element.click()

    def enter_text(self, locator_type, locator_value, text):
        # Método para introducir texto en un elemento de entrada.
        time.sleep(5)
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def swipe(self,start_x=None,start_y=None,end_x=None,end_y=None,duration=None):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_text(self, locator_type, locator_value):
        # Método para obtener el texto de un elemento.
        element = self.find_element(locator_type, locator_value)
        return element.text

    def send_keys(self, keys):
        # Método para enviar teclas al dispositivo.
        self.driver.press_keycode(keys)

    def move_to_element(self,element):
        ui_automator_cmd = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{element}"))'
        self.driver.find_element_by_android_uiautomator(ui_automator_cmd)




