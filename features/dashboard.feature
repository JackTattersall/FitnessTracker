Feature: Dashboard

  Scenario: Add exercise to workout

    Given I am logged in
    And I am on the dashboard screen
    Then I should be presented with a start workout button
    When I press the start workout button
    Then I am redirected to the "Workout" page
    And I should be presented with an add exercise button
    When I click the add exercise button
    Then I should be presented with an add exercise form
    When I submit a valid add exercise form
    Then I should see the exercise populate on the screen
    And The add exercise form should disappear
    When I click the add exercise button
    And I submit a valid add exercise form
    Then I should see the exercise populate on the screen

