from LoginTask import LoginTask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import HTMLTestRunner
import unittest

class LoginTestCase(unittest.TestCase):
    URL = "https://www.saucedemo.com/" # the URL to test
    USERNAME = "standard_user" # the valid username to use
    PASSWORD = "secret_sauce" # the valid password to use
    WRONG_PASSWORD = "secret_spice"

    def setUp(self):
        # create a new Chrome session
        # There is a way to lay the responsability of mantaining the webdriver to a webdrivermanager. Should be something like the following line
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(executable_path= r"chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.login_task = LoginTask(self.driver)


    def tearDown(self):
        # close the browser window
        self.driver.quit()

    # Login Test Case #1: Successful Login
    def test_login_success(self):
        # create a LoginTask object and call the login method with valid credentials
        self.login_task = LoginTask(self.driver)
        self.login_task.login(self.USERNAME, self.PASSWORD)

        # verify that the login was successful by checking the current URL
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "The login was successful")
        
    # Login Test Case #1: Unsuccessful Login - Wrong Password
    def test_login_unsuccessful(self):
        # create a LoginTask object and call the login method with invalid credentials
        self.login_task = LoginTask(self.driver)
        self.login_task.login(self.USERNAME, self.WRONG_PASSWORD)

        # verify that the login was unsuccessful by checking the error message
        is_message_error = self.login_task.is_login_message_as_expected("Epic sadface: Username and password do not match any user in this service")
        self.assertTrue(is_message_error)

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='Reports'))  