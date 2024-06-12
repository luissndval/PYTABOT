from selenium.webdriver.common.by import By

from Appium.elements.elements_Android import Elements
from _pom.front.front import functions


class DropDown(functions):

    def dropDown_Select(self, Option):
        self.driver.swipe(start_x=1000, start_y=1443, end_x=223, end_y=1431, duration=800)
        functions.click_Field(self, By.XPATH, Elements["dropDown Select"])
        # functions.Iframe(self, By.XPATH, Elements["Iframe Options"])
        option_xpath=Elements.get(Option)
        if option_xpath:
            functions.clickAction(self, By.XPATH, option_xpath)

    def DropDown_Validate(self, Option):
        get_text = functions.validates(self, By.XPATH, Elements[Option])
        if Option == get_text:
            functions.screenShot(self, f"Option Validate {get_text}")
