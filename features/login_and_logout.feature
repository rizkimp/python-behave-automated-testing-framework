Feature: login and logout arena
  Scenario: login and logout arena
      Given go to homepage arena
      When  login using username : rizkimahaputra & password : rizkimahaputra
      Then  direct to homepage users
      When  logout
      Then  direct to homepage arena
