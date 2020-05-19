# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/18  15:37
# 文件           :mainPage.py
# IDE            :PyCharm
from base.base import Base
from base.readExel import ReadExel
from base.readYaml import readYaml

data_dir = readYaml()


class MainPage(Base):
    def __init__(self, driver=None, path=None, sheet: str = None):
        super().__init__()
        self.elements = ReadExel(path).readElements(sheet)

    def go_to_contact(self):
        self.find_element_clickable(self.elements.get("通讯录")).click()

        try:
            self.find_element(self.elements.get("姓名"))
            return 1
        except Exception as e :
            print(e)
            return 0




if __name__ == '__main__':
    MainPage(path="../data/data.xlsx", sheet="mainPage").go_to_contact()
