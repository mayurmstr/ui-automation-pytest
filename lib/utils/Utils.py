from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import calendar
import datetime
import json
import random
import re
import uuid
import string
import time
from random import getrandbits
from ipaddress import IPv4Network, IPv4Address
from ipaddress import IPv6Network, IPv6Address


class Utils:

    def __init__(self, objects):
        self.config = objects["config"]
        self.timeout = int(self.config["default_timeout"]) if "default_timeout" in self.config else 120

    def reload_page(self, driver):
        try:
            driver.refresh()
            wait = WebDriverWait(driver, 5)
            wait.until(ec.alert_is_present())
            driver.switch_to.alert.accept()
        except UnexpectedAlertPresentException:
            driver.switch_to.alert.accept()
        except NoAlertPresentException:
            print("No Alert")
        except TimeoutException:
            print("No Alert")

    def return_web_element(self, driver, *element_identifier):
        return driver.find_element(*element_identifier)

    def return_web_elements(self, driver, *element_identifier):
        return driver.find_elements(*element_identifier)

    def wait_element_to_be_visible(self, driver, *element_identifier, time_out=None):
        # wait for element to be visible
        time_out = self.timeout if time_out is None else time_out
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(ec.visibility_of_element_located(element_identifier))
        except TimeoutException as ex:
            print("Exception: " + str(ex.msg))

    def is_element_exists(self, driver, *element_identifier, time_out=None):
        # print(driver.find_elements(*element_identifier))
        # print("Len:", len(driver.find_elements(*element_identifier)))
        # if len(driver.find_elements(*element_identifier)) > 0:
        #     return True
        # return False
        time_out = self.timeout if time_out is None else time_out
        wait = WebDriverWait(driver, time_out)
        try:
            elements = wait.until(ec.presence_of_all_elements_located(element_identifier))
        except NoSuchElementException as ex:
            print("Exception: " + str(ex.msg))
            return False
        except TimeoutException as ex:
            return False
        return True if elements else False

    def wait_element_to_be_clickable(self, driver, *element_identifier, time_out=None):
        # wait for element to be visible
        time_out = self.timeout if time_out is None else time_out
        wait = WebDriverWait(driver, time_out)
        wait.until(ec.element_to_be_clickable(element_identifier))

    def wait_element_to_be_invisibled(self, driver, *element_identifier, time_out=None):
        time_out = self.timeout if time_out is None else time_out
        # wait for element to be visible
        wait = WebDriverWait(driver, time_out)
        wait.until(ec.invisibility_of_element_located(element_identifier))

    def return_element_text(self, driver, *element_identify) -> str:
        text_for_element = Utils.return_web_element(self, driver, *element_identify)
        return text_for_element.text

    def return_elements_text(self, driver, *element_identify):
        text_for_elements = Utils.return_web_elements(self, driver, *element_identify)
        ele_list = []
        for ele in text_for_elements:
            ele_list.append(ele.text)
        ele_list.sort()
        return ele_list

    def return_textarea_element_text(self, driver, *element_identify) -> str:
        text_for_element = Utils.return_web_element(self, driver, *element_identify)
        return text_for_element.get_attribute("value")

    def swtich_to_frame_by_name(self, driver, frame_name):
        driver.switch_to.frame(frame_name)

    def switch_to_default_content(self, driver):
        driver.switch_to.default_content()

    def mouse_hover_to(self, driver, *element_identify):
        ele_to_hover = Utils.return_web_element(self, driver, *element_identify)
        hover = ActionChains(driver).move_to_element(ele_to_hover)
        hover.perform()

    def click_on(self, driver, *element_identify):
        Utils.wait_element_to_be_clickable(self, driver, *element_identify)
        ele = Utils.return_web_element(self, driver, *element_identify)
        ele.click()

    def clear_text_box(self, driver, *element_identify):
        Utils.return_web_element(self, driver, *element_identify).clear()

    def click_on_quick_menu(self, driver, *element_identify):
        # (//img[@class='x-menu-item-icon '])[1]
        ele_to_hover = Utils.return_web_element(self, driver, *element_identify)
        size = ele_to_hover.rect
        # This is also working
        # x_loc = int(size['x']) + int(size['width']) - 10
        # y_loc = int(size['y']) + 13
        # hover = ActionChains(driver).move_by_offset(x_loc, y_loc)
        hover = ActionChains(driver).move_to_element_with_offset(ele_to_hover, int(size['width']) - 10, 13)
        hover.click().perform()

    def drop_down_select(self, driver, *element_identify):
        drop_down = Utils.return_web_element(self, driver, *element_identify)
        return Select(drop_down)

    def select_value_by_name(self, driver, name, *element_identify):
        select = Utils.drop_down_select(self, driver, *element_identify)
        select.select_by_visible_text(name)

    def select_checkbox(self, driver, *element_identify):
        if not Utils.return_web_element(self, driver, *element_identify).is_selected():
            Utils.return_web_element(self, driver, *element_identify).click()

    def unselect_checkbox(self, driver, *element_identify):
        if Utils.return_web_element(self, driver, *element_identify).is_selected():
            Utils.return_web_element(self, driver, *element_identify).click()

    def generate_random_string(self, length=8):
        return ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(length))

    def get_value_of_textbox(self, driver, *element_identify):
        return Utils.return_textarea_element_text(self, driver, *element_identify)

    def get_value_of_checkbox(self, driver, *element_identify):
        if Utils.return_web_element(self, driver, *element_identify).is_selected():
            return "Checked"
        else:
            return "Unchecked"

    def get_selected_text_of_dropdown(self, driver, *element_identify):
        select = Utils.drop_down_select(self, driver, *element_identify)
        return select.first_selected_option.text

    def get_selected_value_of_dropdown(self, driver, *element_identify):
        select = Utils.drop_down_select(self, driver, *element_identify)
        return select.first_selected_option.get_attribute("value")

    def switch_to_window_title(self, driver, tile):
        parent_window = driver.window_handles[0]
        time.sleep(10)
        windows = driver.window_handles
        for window in windows:
            driver.switch_to.window(window)
            if tile == driver.title:
                break
        return parent_window

    def wait_till_other_window_closed(self, driver, time_out=None):
        # wait for element to be visible
        time_out = self.timeout if time_out is None else time_out
        try:
            wait = WebDriverWait(driver, time_out)
            wait.until(ec.number_of_windows_to_be(1))
        except TimeoutException as ex:
            print("Exception: " + str(ex.msg))


    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def generate_instance_id():
        return "i-" + uuid.uuid4().hex[:16]

    @staticmethod
    def generate_random_number():
        return random.randint(1000, 99999)

    @staticmethod
    def generate_random_dns():
        domin = '.'.join([''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(4)),
                          ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(4)),
                          ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(4)),
                          ''.join("com")])
        return domin

    @staticmethod
    def generate_random_netbios():
        return ('_'.join([''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(4)),
                          ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(4)),
                          ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(4))])).upper()

    @staticmethod
    def generate_random_ipv4():
        subnet = IPv4Network("10.0.0.0/8")
        bits = getrandbits(subnet.max_prefixlen - subnet.prefixlen)
        addr = IPv4Address(subnet.network_address + bits)
        return str(addr)

    @staticmethod
    def generate_random_ipv6():
        subnet = '2001:db8:100::/64'
        network = IPv6Network(subnet)
        ipv6address = IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen))
        return str(ipv6address)

    @staticmethod
    def get_next_ip(ip, offset=1):
        subnet = IPv4Network(ip)
        return str(IPv4Address(subnet.network_address + offset))

    @staticmethod
    def get_prev_ip(ip, offset=1):
        subnet = IPv4Network(ip)
        return str(IPv4Address(subnet.network_address - offset))

    @staticmethod
    def convert_epoch_to_datetime(epoch_time):
        if len(str(epoch_time)) > 10:
            epoch_time = epoch_time / 1000
        return str(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(epoch_time)))

    @staticmethod
    def add_days_to_date(date, days):
        date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return str((date + datetime.timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%S'))

    @staticmethod
    def get_date_str_to_date(date):
        return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

    @staticmethod
    def get_current_utc_datetime():
        return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

    @staticmethod
    def convert_datetime_to_epoch(date_time):
        return int(calendar.timegm(time.strptime(date_time, '%Y-%m-%dT%H:%M:%S')))
