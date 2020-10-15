from selenium.webdriver.common.by import By

from lib.elements.LoginElements import LoginElements
from lib.utils.Utils import Utils


class LoginPage(LoginElements):

    def __init__(self, objects):
        self.driver = objects["browser"]
        self.config = objects["config"]
        self.login_url = self.config['url'] + "/index.html"
        self.driver.get(self.login_url)
        self.driver.execute_script("window.onbeforeunload = function() {};")
        self.util = Utils(objects)
        self.util.wait_element_to_be_visible(self.driver, *LoginPage.LOGIN_USERNAME)

    def set_username(self, username):
        username_field = self.util.return_web_element(self.driver, *LoginPage.LOGIN_USERNAME)
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.util.return_web_element(self.driver, *LoginPage.LOGIN_PASSWORD)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.util.return_web_element(self.driver, *LoginPage.LOGIN_BUTTON)
        login_button.click()

    def wait_till_landing_page_loaded(self):
        self.util.wait_element_to_be_visible(self.driver, *LoginPage.CART)

    def do_login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        self.wait_till_landing_page_loaded()
