Feature: Login form

  Scenario: Access the login form and logout screen

    Given an anonymous user
    When I submit a valid login page
    Then I am redirected to the "Dashboard" page

    Given an anonymous user
    When I submit an invalid login page
    Then I am redirected to the "Log-in" page

    Given an anonymous user
    When I submit a valid login page
    Then I am redirected to the "Dashboard" page
    When I logout
    Then I am redirected to the "Logged out" page