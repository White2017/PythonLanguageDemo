# coding:utf-8
"""
  通过configparser模块读取配置文件的信息
"""
import configparser
import os


def readConfig():
    # 创建configparser对象
    conf_obj = configparser.ConfigParser()
    conf_read_path = './config_file/config_read.ini'
    conf_obj.read(conf_read_path)

    # 读取节点为person的name选项对应的值
    name = conf_obj.get('person', 'name')
    print(name)

    # 读取节点为address的city选项对应的值
    city = conf_obj.get('address', 'city')
    print(city)


class ReadConfig(object):
    def __init__(self, conf_read_path=None):
        # 创建configparser对象
        self.conf_obj = configparser.ConfigParser()

        if not os.path.exists(conf_read_path):
            raise FileNotFoundError('error file not found !', conf_read_path)

        # 读取配置文件的所有内容
        self.conf_obj.read(conf_read_path)

    def read_conf_val(self, section, option):
        """
        :brief 获取配置文件节点的选项值
        :param section: 配置文件节点
        :param option: 节点下的选项
        :return: 返回配置文件节点的选项值
        """
        return self.conf_obj.get(section=section, option=option)


if __name__ == "__main__":
    read_config = ReadConfig('./config_file/config_read.ini')
    province = read_config.read_conf_val('address', 'province')
    print(province)
