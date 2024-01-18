Feature: Automation Exercise Website

  Scenario: Add Products to Cart and Verify Details
    Given Navigate to url 'http://automationexercise.com'
    Then Verify that home page is visible successfully
    When Click 'Products' button
    Then Hover over first product and click 'Add to cart'
    Then Click 'Continue Shopping' button
    When Hover over second product and click 'Add to cart'
    Then Click 'View Cart' button
    Then Verify both products are added to Cart
    Then I verify their prices, quantity, and total price
