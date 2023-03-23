from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # locators for the elements on the login page
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        # wait for the username input to be visible and enter the username
        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        # wait for the password input to be visible and enter the password
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        # wait for the login button to be clickable and click it
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
        
    def get_login_error_message(self):
        login_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.LOGIN_ERROR_MESSAGE))
        return login_error_message[0].text