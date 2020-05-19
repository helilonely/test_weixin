# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/18  16:33
# 文件           :get_page.py
# IDE            :PyCharm

from pages.mainPage import MainPage
from pages.contactsPage import ContactsPage
from base.readYaml import readYaml





class GetPage():
    def __init__(self, driver=None):
        self.data_dir = readYaml()
        self.path: str = self.data_dir.get("elements_file")
        self.driver = driver

    def get_main_page(self):
        return MainPage(self.driver,path=self.path,sheet=self.data_dir.get("MainPage"))

    def get_contacts_page(self):
        return ContactsPage(self.driver,path=self.path,sheet=self.data_dir.get("ContactsPage"))
