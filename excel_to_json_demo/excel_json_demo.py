# -*-coding:utf-8-*-
import os

import xlrd
import json


def excelToJson():
    # 打开excel工作簿
    pyPositiondata = xlrd.open_workbook(filename='./myexcelfile/pythonPosition.xlsx')

    # 获取sheet页为'SZPosition'的数据
    # table_SZ = pyPositiondata.sheet_by_name('SZPosition')
    table_SZ = pyPositiondata.sheet_by_index(0)
    # 获取第一行的标题数据
    title = table_SZ.row_values(0)

    # nrows：获取总的行数
    row_numbers = table_SZ.nrows

    with open('pySZPosition.json', 'w') as f:
        f.write('[')
        for row in range(1, row_numbers - 1):
            data = table_SZ.row_values(row)
            # zip：进行键值对的拼接，dict：转换为字典
            dict_data = dict(zip(title, data))
            # dumps: 转换为json字符串
            json_data = json.dumps(dict_data, indent=4, ensure_ascii=False)
            f.write(json_data + ',\n')
        # 将末尾的换行符和逗号剔除
        f.seek(f.tell() - 3, 0)
        f.write(']')


# 封装成类
class ExcelToJson(object):
    def __init__(self, excel_file_path=None, json_path=None, sheet_name=None):
        if not os.path.exists(excel_file_path):
            raise FileNotFoundError('[error] file not found!', excel_file_path)
        # 存储的json的文件路径
        self.json_path = json_path
        # 获取excel文件对象
        self.excel_obj = xlrd.open_workbook(filename=excel_file_path)
        # 获取sheet页对象
        self.sheet_obj = self.excel_obj.sheet_by_name(sheet_name)

    def writeToJson(self):
        """将excel数据转成json格式并保存"""
        # 总行数
        row_numbers = self.sheet_obj.nrows
        # 标题
        title = self.sheet_obj.row_values(0)

        with open(self.json_path, 'w') as f:
            f.write('[')
            for row in range(1, row_numbers - 1):
                data_lst = self.sheet_obj.row_values(row)
                # zip：进行键值对的拼接，dict：转换为字典
                dict_data = dict(zip(title, data_lst))
                # dumps: 转换为json字符串
                json_data = json.dumps(dict_data, indent=4, ensure_ascii=False)
                f.write(json_data + ',\n')
            # 将末尾的换行符和逗号剔除
            f.seek(f.tell() - 3, 0)
            f.write(']')


if __name__ == "__main__":
    excel_to_json = ExcelToJson('./myexcelfile/pythonPosition.xlsx',
                                'pySZPosition.json',
                                'SZPosition')
    excel_to_json.writeToJson()
