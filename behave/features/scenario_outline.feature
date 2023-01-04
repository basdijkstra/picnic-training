Feature: Implementing our first behave specifications

  Scenario Outline: <username> tries to log in to ParaBank
    Given a user <username> with password <password>
    When they submit their credentials
    Then login is <result>
    Examples:
      | username | password  | result       |
      | john     | demo      | successful   |
      | susan    | incorrect | unsuccessful |
      | jimmy    | demo      | successful   |