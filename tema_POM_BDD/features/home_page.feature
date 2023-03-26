Feature: Verify buttons functionality

  Background:
    Given HomePage: the user is on homepage

  Scenario: Verify functionality of Form Authentication button
    When HomePage: user clicks on Form Authentication
    Then LoginPage: user is redirected to Login Page