Feature: View Quotes
View Quotes should do something
Meta:
@verifies #23

Scenario: Should kick user
Scenario: Kick user
Scenario:Kick user with no space
Scenario:Kick user with no space Given
Meta:
@verifies Bug 121

Given a user is logged in
When he posts something illegal
Then he should be kicked off site
And black-listed

Should kick user
Given a Then user logs out
On main page
It should kick him

Feature: Serve coffee
    Coffee should not be served until paid for
    Coffee should not be served until the button has been pressed
    If there is no coffee left then money should be refunded

  Background:
    Given a global administrator named "Greg"
    And a blog named "Greg's anti-tax rants"
    And a customer named "Dr. Bill"
    And a blog named "Expensive Therapy" owned by "Dr. Bill"

  Scenario: Buy last coffee
    Given there are 1 coffees left in the machine
    And I have deposited 1$
    When I press the coffee button
    Then I should be served a coffee

  Scenario Outline: eating
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers

    Examples:
      | start | eat | left |
      |  12   |  5  |  7   |
      |  20   |  5  |  15  |

  Scenario Outline: eating
    Given there are $start cucumbers
    When I eat $eat cucumbers
    Then I should have $left cucumbers

    Examples:
      | start | eat | left |
      |  12   |  5  |  7   |
      |  20   |  5  |  15  |

