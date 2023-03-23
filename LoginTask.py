from LoginPage import LoginPage

class LoginTask:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def login(self, username, password):
        # perform the steps to login with the given username and password
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        
    def login_error_message(self):
        return self.login_page.get_login_error_message()