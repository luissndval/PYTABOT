Feature: Verify Window Switching and Text Availability

  Scenario: Verify text in a newly opened window
    Given I am on the browser, on my mobile device and navigate to "https://rahulshettyacademy.com/AutomationPractice/"
    When I click the "Open Window" button
    Then I should see the "30 day money back guarantee" text
     And I review other training feature texts
