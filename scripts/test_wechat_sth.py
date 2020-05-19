# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/18  16:32
# 文件           :test_wechat_sth.py
# IDE            :PyCharm
import os, sys

import pytest

sys.path.append(os.getcwd())
from pages.get_page import GetPage
from selenium import webdriver

class TestWechart():
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("w3c", False)
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        self.pages = GetPage()

    def teardown_class(self):
        pass

    @pytest.mark.run(order=1)
    def test_wechart_contact(self):
        mainpage = self.pages.get_main_page()
        flag = mainpage.go_to_contact()

        assert flag == 1, "跳转失败"

    @pytest.mark.run(order=2)
    def test_add_member(self):
        contacts_page = self.pages.get_contacts_page()
        contacts_page.add_member()
