from selenium.webdriver.common.by import By

from Appium.elements.elements_Android import Elements
from _pom.front.front import functions


class inToBrowser(functions):
    def Select_Country(self,Country):
        functions.input_Texto(self,By.XPATH,Elements["autoComplete_Country"],Country)
        xpath = Elements["select_Country"].get(Country.strip())
        if xpath:
            try:
                functions.click_Field(self,By.XPATH,xpath)
                functions.screenShot(self, "Country selected successfully")
                return "Country selected successfully."
            except Exception as e:
                return f"Failed to interact with the element: {str(e)}"
        else:
            return "Country code not found in the list."



