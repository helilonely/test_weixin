# -*- encoding=utf8 -*-
# 作者           :heli 
# 创建时间       :2020/5/18  16:20
# 文件           :readYaml.py
# IDE            :PyCharm
import yaml


def readYaml(path="base/data.yaml"):
    '''
    reading  the direction  of  data file  which contains elements locator.
    :param path:
    :return:
    '''
    with open(path,"r", encoding="utf-8") as f:
       data= yaml.safe_load(f)
    return data

if __name__ == '__main__':
    print(readYaml(path="data.yaml"))
