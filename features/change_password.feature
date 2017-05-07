Feature: Change Password

  Scenario: Change password valid

    Given an anonymous user
    When I submit a valid login page
    And I navigate to the change password page
    And I submit a valid change password form
    Then I am redirected to the "Password changed" page
    When I login with username "foo" and password "newpassword"
    Then I am redirected to the "Dashboard" page

  Scenario: Change password invalid

    Given an anonymous user
    When I submit a valid login page
    And I navigate to the change password page
    And I submit an invalid change password form
    Then I am redirected to the "Change your password" page

