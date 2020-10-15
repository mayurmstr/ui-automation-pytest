import pytest
from selenium import webdriver


class Base:
    pass
    # @pytest.fixture(scope="session")
    # def browser(self):
    #     self.driver = webdriver.Firefox()
    #     # self.driver.get('https://qgadmin.p03.eng.sjc01.qualys.com/bo/')
    #
    #     yield self.driver  # provide the fixture value
    #     print("Close Web Browser")
    #     self.driver.close()
    #     self.driver.quit()
