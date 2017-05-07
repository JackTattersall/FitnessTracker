Feature: Login form

  Scenario: Valid login

    Given an anonymous user
    When I submit a valid login page
    Then I am redirected to the "Dashboard" page

  Scenario: Invalid login

    Given an anonymous user
    When I submit an invalid login page
    Then I am redirected to the "Log-in" page

  Scenario: Logout redirects to correct page

    Given an anonymous user
    When I submit a valid login page
    Then I am redirected to the "Dashboard" page
    When I logout
    Then I am redirected to the "Logged out" page