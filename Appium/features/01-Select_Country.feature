Feature: Autocomplete Suggestion Test, I want to use the complete suggestion field to correctly select Countries

  Scenario Outline: Select "<Country>" , using the autocomplete field.
    Given I am on the browser, on my mobile device and navigate to "https://rahulshettyacademy.com/AutomationPractice/"
    When  I enter "<Country>" into the suggestion class automcomplete field
    Then I should have correctly selected the countries
    Examples:
      | Country              |
      | ME                   |
      | UNI                  |
      | United Arab Emirates |


