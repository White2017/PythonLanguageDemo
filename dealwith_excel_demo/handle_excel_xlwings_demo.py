# coding:utf-8  fxb_qzyx@163.com
"""
   使用第三方库(xlwings):来处理excel
"""
import os
import traceback

import xlwings as xw
import pandas as pd


class ParseExcel(object):
    def __init__(self, excel_file_path):
        if not os.path.exists(excel_file_path):
            raise FileNotFoundError('[error] file not exist!', excel_file_path)

        try:
            # visible=false:不出现excel的图形界面;  add_book=False:只打开，不新建工作簿
            self.app = xw.App(visible=False, add_book=False)
            # 获取excel工作簿对象
            self.wb_obj = self.app.books.open(excel_file_path)
        except Exception as e:
            traceback.print_exc()

    def getCell(self, sheet_name, row, col):
        """
        :brief 获取excel单元格值
        :param sheet_name: excel的sheet页名称
        :param row: excel的行坐标
        :param col: excel的列坐标
        :return: 返回excel的单元格值
        """
        sheet_obj = self.wb_obj.sheets[sheet_name]
        cell_val = sheet_obj.range((row, col)).value
        return cell_val

    def getRange(self, sheet_name, min_row, min_col, max_row, max_col):
        """
         :brief 获取多行单元格的数据(包括一行/一列)，以列表的形式返回
         :param sheet_name: sheet页名称
         :param min_row: 左上角的行号
         :param min_col: 左上角的列号
         :param max_row: 右下角的行号
         :param max_col: 右下角的列号
         :return: 以列表的形式返回多行单元格的数据
         """
        # 获取excel的sheet页对象
        sheet_obj = self.wb_obj.sheets[sheet_name]
        # 获取excel指定的单元格所有数据
        data_list = sheet_obj.range((min_row, min_col), (max_row, max_col)).value
        return data_list

    def setCell(self, sheet_name, row, col, val):
        """
        :brief 给excel单元格添加数据
        :param sheet_name: excel的sheet页名称
        :param row: excel行坐标
        :param col: excel 列坐标
        :param val: 要填充的值
        :return: None
        """
        # 获取excel的sheet页对象
        sheet_obj = self.wb_obj.sheets[sheet_name]
        # 给excel的单元格填充数据
        sheet_obj.range((row, col)).value = val

    def setTable(self, sheet_name, row, col, val):
        """
        :brief 将一组数据填充到excel构成的多行多列中
        :param sheet_name: excel的sheet页名称
        :param row: excel的行坐标
        :param col: excel的列坐标
        :param val: 可以是二维数组 和 DataFrame类型的数据
        :return: None
        """
        sheet_obj = self.wb_obj.sheets[sheet_name]

        if isinstance(val, list):  # 列表类型的数据回填
            sheet_obj.range((row, col)).options(extend='table').value = val

        # elif isinstance(val, pd.DataFrame):
        else:  # DataFrame类型的数据回填
            sheet_obj.range((row, col)).options(index=False, header=False).value = val

    def save(self):
        """保存并退出excel"""
        self.wb_obj.save()
        self.wb_obj.close()
        self.app.quit()


if __name__ == "__main__":
    parse_excel = ParseExcel('./excel_file/ExcelData.xlsx')
    # parse_excel.getCell('massage', 1, 1)
    print(parse_excel.getRange('massage', 1, 1, 3, 4))
    # # parse_excel.setCell('massage', 10, 10, 'python')
    # parse_excel.setTable('massage', 11, 11, 'helo')
    parse_excel.save()
