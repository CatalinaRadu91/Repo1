Feature: Login feature

  Background:
    Given LoginPage: the user is on login page

  @validcredentials
  Scenario Outline: Login successfully (with valid credentials)
    When LoginPage: user enters valid <username> and valid <password> and presses login button
    Then SecurePage: user is redirected to secure page

    Examples:
      | username | password             |
      | tomsmith | SuperSecretPassword! |


  @invalidusername
  Scenario Outline: Login with invalid username
    When LoginPage: user enters invalid <username> and valid <password> and presses login button
    Then LoginPage: user sees an error message

    Examples:
      | username | password             |
      | alabala  | SuperSecretPassword! |

  @invalidpassword
  Scenario Outline: Login with invalid password
    When LoginPage: user enters valid <username> and invalid <password> and presses login button
    Then LoginPage: user sees an error message: " Your password is invalid!"

    Examples:
      | username | password             |
      | tomsmith | supersecretpassword! |


  @invalidcredentials
  Scenario: Login with invalid credentials
    When LoginPage: user enters invalid username and invalid password and presses login button
    Then LoginPage: user sees an error message: "Your username is invalid!"