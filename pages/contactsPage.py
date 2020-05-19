# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/19  16:53
# 文件           :contactsPage.py
# IDE            :PyCharm
from base.base import Base
from base.readExel import ReadExel




class ContactsPage(Base):
    def __init__(self, driver=None, path:str=None,sheet:str=None):
        super().__init__()
        self.elements = ReadExel(path).readElements(sheet)

    def add_member(self):
        self.find_element_clickable(self.elements.get("添加成员")).click()

        try:
            # self.find_element(self.elements.get("姓名"))
            return 1
        except Exception as e :
            print(e)
            return 0



if __name__ == '__main__':
    ContactsPage(path="../data/data.xlsx", sheet="通讯录").add_member()

