import time

from selenium.webdriver.common.by import By

from BDD.element.elements import elements
from _pom.front.front import functions


class addProduct(functions):
    def addProduct(self):
        functions.click_While(self, By.XPATH, elements["addProduct"][0])
        functions.screenShot(self, "Visualizacion de Productos.")
        functions.click_Field(self, By.XPATH, elements["addProduct"][1])
        functions.click_Field(self, By.XPATH, elements["addProduct"][2])
        functions.click_While(self, By.XPATH, elements["addProduct"][3])
        functions.screenShot(self, "add to cart")
        time.sleep(2)
