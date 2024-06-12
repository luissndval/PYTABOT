Feature: Autocomplete Suggestion Test, I want to use the complete suggestion field to correctly select Countries

  Scenario Outline: Select "<Country>" , using the autocomplete field.
    Given open saucelabs
    Examples:
      | Country              |
      | ME                   |
#      | UNI                  |
#      | United Arab Emirates |
#

