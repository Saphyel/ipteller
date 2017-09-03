Feature: You get a notification

Scenario: I should get a message
    When I want to send an email with the subject "test 1" and body "This is a test"
    Then I expect to get it with a proper format
