Feature: Select Options from a dropdown.

  Scenario Outline:Selecting and verifying options in a dropdown menu
    Given I am on the browser, on my mobile device and navigate to "https://rahulshettyacademy.com/AutomationPractice/"
    When  I select "<Option>" from the Dropdown
    Then the dropdown should display "<Option>" as selected

    Examples:
      | Option   |
      | Option 1 |
      | Option 2 |
      | Option 3 |

