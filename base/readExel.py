# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/18  15:45
# 文件           :readExel.py
# IDE            :PyCharm
import xlrd


class ReadExel(object):

    def __init__(self, path: str = "../data/data.xlsx"):
        self._path = path

    def readElements(self, sheet_name: str = "通讯录"):
        '''
        读取的信息是元素   第一行是标题  ，name ,by ,value. 分别是定位的元素名称（自定义），方式，值。
        :param sheet_name:
        :return:
        '''
        dict_lines = {}
        wb = xlrd.open_workbook(self._path)
        table = wb.sheet_by_name(sheet_name)
        for nrow in range(1, table.nrows):
            dict_lines[table.cell_value(nrow, 0)] = (table.cell_value(nrow, 1), table.cell_value(nrow, 2))

        return dict_lines

    def readCases(self, sheet_name: str = "cases"):
        list_cases =[]
        wb = xlrd.open_workbook(self._path)
        table = wb.sheet_by_name(sheet_name)

        for nrow in range(1, table.nrows):
            dict_case = {}
            dict_case["num"]=table.cell_value(nrow,0)
            dict_case["by"]=table.cell_value(nrow,3)
            dict_case["value"]=table.cell_value(nrow,4)
            dict_case["operate"]=table.cell_value(nrow,5)
            list_cases.append(dict_case)
        return list_cases



if __name__ == '__main__':
    print(ReadExel().readElements())
    # print(ReadExel().readCases())
