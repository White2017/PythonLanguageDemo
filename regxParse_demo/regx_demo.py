# coding=utf-8

import re


def GetLegalCaseName(old_case_name):
    """
    brief 根据原有的用例名生成合法的用例名
    :param old_case_name:传入的用例名
    :return: 返回合法的用例名
    """
    regex = r"\W"  # 匹配非字母、数字、下划线的任意字符
    reObj = re.compile(regex)
    new_case_name = "AP_" + reObj.sub("_", old_case_name)
    print(new_case_name)
    return new_case_name


if __name__ == "__main__":
    old_case_name = "15-16@Comprsion+right5.14HZ"
    GetLegalCaseName(old_case_name)
    help(GetLegalCaseName)
