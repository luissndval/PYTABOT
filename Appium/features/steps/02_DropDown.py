from behave import *

from Appium.page.Drop_Dpwn.Dropdown_Validate import DropDown


@when(u'I select "{Option}" from the Dropdown')
def Select_option(context,Option):
    try:
        DropDown.dropDown_Select(context,Option)
    except:
        assert False, f"Error in :'{Select_option}'"

@then(u'the dropdown should display "{Options}" as selected')
def step_impl(context,Option):
    try:
        DropDown.dropDown_Select(context, Option)
    except:
        assert False, f"Error in :'{Select_option}'"
