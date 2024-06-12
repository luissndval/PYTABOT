from selenium.webdriver.common.by import By

from Appium.elements.elements_Android import Elements
from _pom.front.front import functions


class Validate(functions):


    def validate_country(self):
        validates={"Mexico",
                   "United States (USA)",
                   "United Arab Emirates"
                   }
        text=functions.validates(self,By.XPATH,Elements["autoComplete_Country"])

        if text in validates:
            functions.screenShot(self,f"Country Validate {text}")
        else:
            assert False, "The Country does exist."



