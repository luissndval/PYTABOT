from behave import *

from Appium.page.Select_Country.Validate_country import Validate
from Appium.page.Select_Country.inTo_browser import inToBrowser
from Appium.page.Select_Country.open_Mobile_And_See_Main_Menu import Mobile_device


@given(u'I am on the browser, on my mobile device and navigate to "https://rahulshettyacademy.com/AutomationPractice/"')
def Open_Mobile_device(context):
    try:
        Mobile_device.openMobile(context)
        Mobile_device.url_Text(context)
    except:
        context.driver.quit()
        assert False, f"Error in :'{Open_Mobile_device}'"


@when(u'I enter "{Country}" into the suggestion class automcomplete field')
def Autocomplete_Field(context,Country):
    try:
        inToBrowser.Select_Country(context,Country)
    except:
        context.driver.quit()
        assert False,f"Error in :'{Autocomplete_Field}'"


@then(u'I should have correctly selected the countries')
def correctly_selected(context):
    try:
        Validate.validate_country(context)
        context.driver.quit()
    except:
        context.driver.quit()
        assert False,f"Error in :'{correctly_selected}'"

