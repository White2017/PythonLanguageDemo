# coding:utf-8
import os
import sys


def getEnvironmentPath():
    """
    :biref ；获取系统环境变量的值
    :return: 返回系统环境变量的值(字符串)
    """
    environment_path = os.environ['PATH']
    return environment_path


def getPythonVersion():
    """获取python的版本"""
    py_version = sys.version_info[0]
    return py_version



if __name__ == "__main__":
    print(getPythonVersion())
