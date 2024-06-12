from Appium.page.sauceLabs.sauceLabs import sauceLabs
from behave import *


@given(u'open saucelabs')
def Open_Mobile_device(context):
    try:
        sauceLabs.openMobile(context)
    except:
        context.driver.quit()
        assert False, f"Error in :'{Open_Mobile_device}'"
