import pytest
import os
import time
from selenium import webdriver
from pathlib import Path
# from selenium.webdriver.chrome.options import Options
from lib.utils.ConfigParser import ConfigParser
from lib.utils.Utils import Utils

driver = None
r_path = None


def pytest_addoption(parser):
    parser.addoption("--conf_file", action="store", default="config.cfg", help="Provide Config File Name")
    parser.addoption("--op_path", action="store", default="", help="Provide Output Dir Path")


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    # pref=""
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture(scope="session")
def conf_file(request):
    return request.config.getoption("--conf_file")


@pytest.fixture(scope="session")
def op_path(request):
    return request.config.getoption("--op_path")


@pytest.fixture(scope="session")
def config(conf_file):
    return ConfigParser(conf_file).get_all_options('DEFAULT')


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever tests fails.
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever tests fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             import hashlib
#             names = report.nodeid.split("::")
#             classname = '.'.join(names[:-1])
#             feature_request = item.funcargs['request']
#             r_path = feature_request.getfixturevalue('op_path')
#             screenshot_dir = os.path.join(r_path, classname)
#             if not os.path.exists(screenshot_dir):
#                 os.makedirs(screenshot_dir)
#             name = hashlib.md5(u'{0}'.format(names[-1]).encode('utf-8', 'ignore')).hexdigest()
#             screenshot_file_name = '{0}.png'.format(name)
#             file_name = os.path.join(screenshot_dir, screenshot_file_name)
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra


@pytest.fixture(scope='session')
def browser(config):
    global driver
    if driver is None:
        if 'browser' not in config and 'os' not in config:
            print("Browser/OS is not defined in config file")
            exit(1)
        else:
            project_dir = os.path.dirname(__file__) + '/..'
            driver_dir = os.path.join(project_dir, 'drivers', config['os'])
            if config['browser'] == 'firefox':
                options = webdriver.FirefoxOptions()
                options.add_argument("--start-maximized")
                options.add_argument('--ignore-certificate-errors')
                if 'headless' in config and config['headless'] == 'True':
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                    options.add_argument('--disable-dev-shm-usage')
                    options.add_argument('--no-sandbox')
                if config['os'] == 'windows':
                    driver_path = os.path.join(driver_dir, 'geckodriver.exe')
                elif config['os'] == 'linux':
                    driver_path = os.path.join(driver_dir, 'geckodriver')
                driver = webdriver.Firefox(executable_path=driver_path, options=options)
            elif config['browser'] == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                options.add_argument('--ignore-certificate-errors')
                if 'headless' in config and config['headless'] == 'True':
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                    options.add_argument('--disable-dev-shm-usage')
                    options.add_argument('--no-sandbox')
                if config['os'] == 'windows':
                    driver_path = os.path.join(driver_dir, 'chromedriver.exe')
                elif config['os'] == 'linux':
                    driver_path = os.path.join(driver_dir, 'chromedriver')
                else:
                    driver_path = os.path.join(driver_dir, 'chromedriver.exe')
                driver = webdriver.Chrome(executable_path=driver_path, options=options)


        driver.accept_untrusted_certs = True

    yield driver  # provide the fixture value
    # driver.refresh()
    # # driver.switch_to.alert.accept()
    # time.sleep(10)
    print("Close Web Browser")
    # driver.find_element_by_xpath("//a[contains(@id,'logout_sidebar_link')]").click()
    # driver.close()
    # driver.quit()

    return driver


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture(scope="session")
def objects(browser, config):
    obj_dict = {
        'browser': browser,
        'config': config,
    }
    return obj_dict
