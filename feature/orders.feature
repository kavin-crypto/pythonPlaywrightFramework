Feature: Orders history page interactions
  As a logged-in user
  I want the UI to behave correctly when the backend is intercepted
  So that I can validate the edge cases by seeing no orders are returned

    Scenario: No orders are returned when the orders API is intercepted
    Given the orders API is stubbed to return no orders
    When the user logs in
    And the user navigates to the orders page
    Then the user sees a no orders message