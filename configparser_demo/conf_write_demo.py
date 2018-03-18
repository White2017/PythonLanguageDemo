# coding:utf-8
"""通过configparser模块将信息写入配置文件"""

import configparser

import os


def writeConfig():
    # 创建配置文件对象
    conf_obj = configparser.ConfigParser()

    # 添加节点
    conf_obj.add_section('information')

    # 给节点section写入option
    conf_obj.set('information', 'name', 'Tom')
    conf_obj.set('information', 'age', '20')

    # 保存到配置文件中
    conf_obj.write(open('./config_file/config_write.ini', 'w+'))

#封装成类
class WriteConfig(object):
    def __init__(self, write_config_path):
        # 创建配置文件对象
        self.conf_obj = configparser.ConfigParser()
        # 若存在配置文件，则读取其内容
        if os.path.exists(write_config_path):
            self.conf_obj.read(write_config_path)

        self.write_config_path = write_config_path

    def addSection(self, section):
        """
        :brief : 向配置文件（xx.ini）中添加新的节点(section)
        :param section: 要添加的节点
        :return: None
        """
        self.conf_obj.add_section(section=section)

    def writeOption(self, section, option, val):
        """
        :brief :向配置文件写入内容
        :param section: 节点名称
        :param option: 节点下的选项
        :param val: 节点选项对应的值
        :return: None
        """
        try:  # 若不存在该节点，则新建
            self.conf_obj.add_section(section=section)
        except:
            pass

        self.conf_obj.set(section=section, option=option, value=val)

    def save(self):
        """保存内容"""
        self.conf_obj.write(open(self.write_config_path, 'w+'))


if __name__ == "__main__":
    write_config = WriteConfig('./config_file/config_write.ini')
    write_config.writeOption('information', 'age', '20')
    write_config.save()

