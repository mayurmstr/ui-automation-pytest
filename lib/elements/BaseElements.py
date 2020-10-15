from selenium.webdriver.common.by import By


class BaseElements:
    CART = (By.XPATH, "//div[@id='shopping_cart_container']")
    LOGOUT_LINK = (By.XPATH, "//a[contains(@id,'logout_sidebar_link')]")
