from LoginPage import LoginPage

class LoginTask:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def enter_username(self, username):
        # wait for the username input to be visible and enter the username
        username_input = self.login_page.get_username_textfield()
        username_input.clear()
        username_input.send_keys(username)
        
    def enter_password(self, password):
        # wait for the password input to be visible and enter the password
        password_input = self.login_page.get_password_textfield()
        password_input.clear()
        password_input.send_keys(password)
        
    def click_login_button(self):
        # wait for the login button to be clickable and click it
        login_button = self.login_page.get_login_button()
        login_button.click()

    def login(self, username, password):
        # perform the steps to login with the given username and password
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
    def is_login_message_as_expected(self, expected_message):
        return self.login_page.get_login_error_message_label().text == expected_message