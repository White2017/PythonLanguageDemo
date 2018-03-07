# coding=utf-8

import re


def GetLegalCaseName(oldCaseName):
    """
    '''根据原有的用例名生成合法的用例名'''
    :param oldCaseName:传入的用例名
    :return: 返回合法的用例名
    """
    regex = r"\W"  # 匹配非字母、数字、下划线的任意字符
    reObj = re.compile(regex)
    newCaseName = "AP_" + reObj.sub("_", oldCaseName)
    print(newCaseName)
    return newCaseName


if __name__ == "__main__":
    oldCaseName = "15-16@Comprsion+right5.14HZ"
    GetLegalCaseName(oldCaseName)
    help(GetLegalCaseName)
