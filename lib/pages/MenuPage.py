import time
from lib.elements.MenuElements import MenuElements
from lib.utils.Utils import Utils


class MenuPage(MenuElements):

    def __init__(self, objects):
        self.driver = objects["browser"]
        self.config = objects["config"]
        self.util = Utils(objects)

    def reload_bo_page(self):
        self.driver.refresh()

    def go_to_dashboard_page(self):
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.DASHBOARD_LINK)
        dashboard_link = self.util.return_web_element(self.driver, *MenuPage.DASHBOARD_LINK)
        dashboard_link.click()

    def go_to_assets(self):
        # self.util.reload_page(self.driver)
        self.util.wait_element_to_be_invisibled(self.driver, *MenuPage.LOADING_MSG)
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.ASSETS_LINK)
        self.util.click_on(self.driver, *MenuPage.ASSETS_LINK)

    def go_to_scans(self):
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.SCANS_LINK)
        self.util.click_on(self.driver, *MenuPage.SCANS_LINK)

    def go_to_reports(self):
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.REPORTS_LINK)
        self.util.click_on(self.driver, *MenuPage.REPORTS_LINK)

    def go_to_remediation(self):
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.REMEDIATION_LINK)
        self.util.click_on(self.driver, *MenuPage.REMEDIATION_LINK)

    def go_to_knowledgebase(self):
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.KNOWLEDGEBASE_LINK)
        self.util.click_on(self.driver, *MenuPage.KNOWLEDGEBASE_LINK)

    def go_to_users(self):
        self.util.wait_element_to_be_visible(self.driver, *MenuPage.USERS_LINK)
        self.util.click_on(self.driver, *MenuPage.USERS_LINK)

    def is_login_success(self):
        return self.util.is_element_exists(self.driver, *MenuPage.CART)
