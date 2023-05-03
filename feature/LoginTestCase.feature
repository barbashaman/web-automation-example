Feature: Login to Sauce Demo
As a User
I wanto to login to Sauce Demo website
Sp that I can access the products page

Scenario: Successful login with valid credentials
Given I am on "https://www.saucedemo.com/" website
When I enter "standard_user" in field with "id" equal to "user-name"
And I enter "secret_sauce" in field with "id" equal to "password"
And I click the button with "id" equal to "login-button"
Then I should see the "https://www.saucedemo.com/inventory.html" page