from behave import *

from BDD.pages.initial.browser import browser
from BDD.pages.login.LoginCode import login


@given(u'que el usuario está en la página web de la aplicación Pais: "{country_code}" Brand: "{brand}"')
def step_impl(context, country_code, brand):
    browser.start_browser(context, country_code, brand)


@when(u'el usuario hace clic en "Iniciar Sesión" e ingresa email: "{email}" y password: "{password}"')
def step_impl(context, email, password):
    login.loginUser(context, email, password)
