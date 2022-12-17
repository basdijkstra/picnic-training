Feature: Add items to cart
  Demo to show that we can add items to a cart

  Scenario: Two of the same items can be added to the cart in a single transaction
    Given Bob has an empty shopping cart
    When he adds two backpacks to the cart
    Then the number of items in his shopping cart is 2
    And he can proceed to the checkout page