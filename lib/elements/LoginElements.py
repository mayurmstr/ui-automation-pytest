from selenium.webdriver.common.by import By

from lib.elements.BaseElements import BaseElements


class LoginElements(BaseElements):
    LOGIN_USERNAME = (By.ID, 'user-name')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
