Feature: login and logout arena
  Scenario: login and logout arena
      Given go to homepage arena
      When  login using username : richard & password : 12345678
      Then  direct to homepage users
      When  logout
      Then  direct to homepage arena
