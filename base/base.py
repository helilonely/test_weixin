# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/18  12:49
# 文件           :base.py
# IDE            :PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import TouchActions

webdriver.Chrome()


class Base(object):
    def __init__(self, driver=None):
        '''  默认使用的是chrome浏览器，
        :param driver: 传入的值是driver
        :param browser:
        '''
        if (driver == None):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("w3c", False)
            options.debugger_address="127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
        else:
            self._driver = driver


    def find_element(self, locator: tuple, timeout=10, frequency=0.5):
        return WebDriverWait(self._driver, timeout=timeout, poll_frequency=frequency).until(
            lambda x: x.find_element(*locator))

    def find_element_clickable(self, locator: tuple, timeout=10, frequency=0.5):
        return WebDriverWait(self._driver, timeout=timeout, poll_frequency=frequency).until(
            EC.element_to_be_clickable(locator))

    def send_keys(self, locator, text, timeout=10, frequency=0.5):
        self.find_element_clickable(locator, timeout, frequency).send_keys(text)

    def scroll_screen(self):
        '''
        仅当chrome时有效
        :return:
        '''
        y = self._driver.get_window_size().get("height")
        ac = TouchActions(self._driver)
        ac.scroll(0, y * 0.6).perform()

    def get_text(self,locator: tuple, timeout=10, frequency=0.5):
        return self.find_element(locator, timeout, frequency).text





if __name__ == '__main__':
    ba = Base()
    print(ba._driver,type(ba._driver))
    ba._driver.get("https://www.baidu.com")
    ba.find_element_clickable((By.ID, "kw")).send_keys("cctv")
    ba.send_keys((By.ID, "kw"), Keys.ENTER)
    time.sleep(0.5)
    ba.scroll_screen()
    time.sleep(10)
    ba._driver.quit()
