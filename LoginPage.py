from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # locators for the elements on the login page
    
    
    USERNAME_INPUT = (By.ID, "user-name")
    # USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def get_username_textfield(self):
        # searches for the username input
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        

    def get_password_textfield(self):
        # searches for the password input
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))

    def get_login_button(self):
        # searches for the login button
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        
        
    def get_login_error_message_label(self):
        # searches for the login error message_label
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_ERROR_MESSAGE))