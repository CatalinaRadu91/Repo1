Feature: Verify functionality of Secure Page

  Background:
    Given SecurePage: the user is on secure_page

  Scenario: Verify that user can logout successfully
    When SecurePage: user clicks on logout button
    Then LoginPage: user is directed to Login Page