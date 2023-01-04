Feature: practice using the behave context

  Scenario Outline: Calculator performs addition
    Given a number <first_number>
    And another number <second_number>
    When I add these numbers
    Then the result is <result>
    Examples:
      | first_number | second_number | result |
      | 2            | 3             | 5      |
      | 987          | 13            | 1000   |
      | 5            | 5             | 10     |