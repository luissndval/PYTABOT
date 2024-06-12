from selenium.webdriver.common.by import By

from BDD.element.elements import elements
from _pom.front.front import functions


class login(functions):

    def loginUser(self, email, password):
        functions.click_Field(self, By.XPATH, elements["logIn"][0])
        functions.click_Field(self, By.XPATH, elements["logIn"][1])
        functions.input_Texto(self, By.XPATH, elements["logIn"][2], email)
        functions.input_Texto(self, By.XPATH, elements["logIn"][3], password)
        functions.click_Field(self, By.XPATH, elements["logIn"][4])
        functions.click_Field(self, By.XPATH, elements["logIn"][5])
        functions.screenShot(self, "Inicio Sesion")
