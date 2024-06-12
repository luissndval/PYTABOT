from behave import *

from BDD.pages.payment.payment_options import buy


@then(u'el usuario concreta la compra y obtiene el numero de orden.')
def step_impl(context):
    try:
        buy.Shipping(context)
        buy.Select_Shipping_Price(context)
        buy.Payment(context)
        buy.OrderReview(context)
    except:
        context.driver.close()

