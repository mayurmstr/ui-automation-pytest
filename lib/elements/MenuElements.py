from selenium.webdriver.common.by import By

from lib.elements.BaseElements import BaseElements


class MenuElements(BaseElements):
    DASHBOARD_LINK = (By.XPATH, "//a[@href='/fo/home/Dashboard.php?skip=1'][contains(.,'Dashboard')]")
    SCANS_LINK = (By.XPATH, "//a[@href='/fo/scan/scanList.php'][contains(.,'Scans')]")
    REPORTS_LINK = (By.XPATH, "//a[@href='/fo/report/report_list.php'][contains(.,'Reports')]")
    REMEDIATION_LINK = (By.XPATH, "//a[@href='/fo/remedy/index.php'][contains(.,'Remediation')]")
    #ASSETS_LINK = (By.XPATH, "//a[@href='/fo/tools/assetGroups.php'][contains(.,'Assets')]")
    ASSETS_LINK = (By.XPATH, "//a[contains(text(),'Assets')]")
    KNOWLEDGEBASE_LINK = (By.XPATH, "//a[@href='/fo/tools/kbase.php'][contains(.,'KnowledgeBase')]")
    USERS_LINK = (By.XPATH, "//a[@href='/fo/tools/userAccounts.php'][contains(.,'Users')]")

