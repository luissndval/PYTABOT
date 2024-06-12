from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from BDD.element.elements import elements
from _pom.front.front import functions


class buy(functions):

    def Shipping(self):
        functions.click_While(self, By.XPATH, elements["Shipping"][0])
        functions.input_Texto(self, By.XPATH, elements["Shipping"][1],"Valor 1")
        functions.input_Texto(self, By.XPATH, elements["Shipping"][2], "Valor 2")
        functions.input_Texto(self, By.XPATH, elements["Shipping"][3], "1406")
        functions.input_Texto(self, By.XPATH, elements["Shipping"][4], "1150163632")
        functions.click_Field(self,By.XPATH,elements["Shipping"][5])
        functions.key_Up_Key_Down(self,Keys.DOWN)
        functions.key_Up_Key_Down(self, Keys.ENTER)
        functions.click_While(self, By.XPATH, elements["Shipping"][6])
        functions.screenShot(self, "Info Shipping")

    def Select_Shipping_Price(self):
        functions.click_While(self, By.XPATH, elements["Select_Shipping_Price"][0])
        functions.screenShot(self, "Info Shipping")
        functions.click_While(self, By.XPATH, elements["Shipping"][6])


    def Payment(self):
        functions.screenShot(self, "Info Shipping")
        functions.click_While(self, By.XPATH, elements["Shipping"][6])

    def OrderReview(self):
        functions.screenShot(self, "OrderReview")
        functions.click_While(self, By.XPATH, elements["Payment"][0])
