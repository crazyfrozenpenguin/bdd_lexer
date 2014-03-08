#!/usr/bin/python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from bdd import BDDLexer

print '<head><style>'
print HtmlFormatter().get_style_defs('.highlight')
print '</style></head><body>'


code = 'Feature: View Quotes\n' \
    'View Quotes should do something\n' \
    'Meta:\n' \
    '@verifies G989\n' \
    '\n' \
    'Scenario: Should kick user\n' \
    'Scenario: Kick user\n' \
    'Scenario:Kick user with no space\n' \
    'Scenario:Kick user with no space Given\n' \
    'Meta:\n' \
    '@verifies R1231\n' \
    '\n' \
    'Given a user is logged in\n' \
    'When he posts something illegal\n' \
    'Then he should be kicked off site\n' \
    'And black-listed\n'
print highlight(code, BDDLexer(), HtmlFormatter())

code = 'Should kick user\n' \
    'Given a Then user logs out\n' \
    'On main page\n' \
    'It should kick him\n'
print highlight(code, BDDLexer(), HtmlFormatter())

code = """Feature: Serve coffee
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
      |  20   |  5  |  15  |"""
print highlight(code, BDDLexer(), HtmlFormatter())

print '</body>'

