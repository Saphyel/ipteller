Feature: Update your old IP address

Scenario: I want to save an IP and able to read it
    Given I have the entity in address.txt
    When I save the IP 2.2.2.2
    Then I expect to load it
