Feature: Return IP from JsonIP provider

Scenario: Get your IP address
    When I want to check my IP address
    Then I expect to get a string
