from behave import *

from BDD.pages.main_actions.addProductPage import addProduct


@when(u'el usuario agrega productos al carrito')
def step_impl(context):
    addProduct.addProduct(context)


