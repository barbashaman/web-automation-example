from LoginTask import LoginTask
from selenium import webdriver
import unittest



class LoginTestCase(unittest.TestCase):
    URL = "https://www.saucedemo.com/" # the URL to test
    USERNAME = "standard_user" # the valid username to use
    PASSWORD = "secret_sauce" # the valid password to use
    WRONG_PASSWORD = "not_so_secret"

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.login_task = LoginTask(self.driver)


    def tearDown(self):
        # close the browser window
        self.driver.quit()

    def test_login_success(self):
        # create a LoginTask object and call the login method with valid credentials
        self.login_task = LoginTask(self.driver)
        self.login_task.login(self.USERNAME, self.PASSWORD)

        # verify that the login was successful by checking the current URL
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "The login was successful")
        
    def test_login_unsuccessful(self):
        # create a LoginTask object and call the login method with invalid credentials
        self.login_task = LoginTask(self.driver)
        self.login_task.login(self.USERNAME, self.WRONG_PASSWORD)

        # verify that the login was unsuccessful by checking the error message
        error_message = self.login_task.login_error_message()
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", error_message, "The login was not successful")

if __name__ == '__main__':
    unittest.main()  