# coding:utf-8  fxb_qzyx@163.com
"""
   使用第三方库(xlrd):来读取excel的内容
"""
import os
import traceback

import xlrd


class ParseExcel(object):
    def __init__(self, excel_file_path):
        if not os.path.exists(excel_file_path):
            raise FileNotFoundError('[error] file not exist!', excel_file_path)

        try:
            # 获取excel工作簿对象
            self.wb_obj = xlrd.open_workbook(excel_file_path)
        except Exception as e:
            traceback.print_exc()

    def reduceOne(self, row=None, col=None):
        """
        :brief 将传入的行/列号减1，保证索引以1开始
        :param row: 行号
        :param col: 列号
        :return: 返回减1后的行/列号
        """
        if row and col:
            row -= 1
            col -= 1
            return row, col
        elif row and col == None:
            row -= 1
            return row
        elif row == None and col:
            col -= 1
            return col
        else:
            return None

    def getCell(self, sheet_name, row, col):
        """
        :brief 获取excel单元格的值
        :param sheet_name: sheet页名称
        :param row: 行号
        :param col: 列号
        :return: 返回单元格的值
        """
        # 获取sheet页对象
        sheet_obj = self.wb_obj.sheet_by_name(sheet_name)
        # 行/列值减1，保证索引号以1开始
        row, col = self.reduceOne(row, col)
        # 获取单元格的值
        # cell_data = sheet_obj.cell_value(row, col)
        cell_data = sheet_obj.cell(row, col).value
        # 返回单元格的值
        return cell_data

    def getRows(self, sheet_name, rowx, start_colx=1, end_colx=None):
        """
        :brief 获取指定行的起止列的数据
        :param sheet_name: sheet页名称
        :param rowx: 行号
        :param start_colx: 起始列号
        :param end_colx: 结束列号
        :return: 以列表形式返回获取的指定行的起止列的数据
        """
        # 获取sheet页对象
        sheet_obj = self.wb_obj.sheet_by_name(sheet_name)
        # rowx/start_colx减1：end_colx不用减1(源码采用的切片取值，切片是左闭右开型)
        rowx, start_colx = self.reduceOne(rowx, start_colx)
        row_data_list = sheet_obj.row_values(rowx, start_colx=start_colx, end_colx=end_colx)
        return row_data_list

    def getColumns(self, sheet_name, colx, start_rowx=1, end_rowx=None):
        """
        :brief 获取指定列的起止行的数据
        :param sheet_name: sheet页名称
        :param colx: 列号
        :param start_rowx: 起始行号
        :param end_rowx: 结束行号
        :return: 以列表形式返回获取的指定列的起止行的数据
        """
        # 获取sheet页对象
        sheet_obj = self.wb_obj.sheet_by_name(sheet_name)
        # rowx, start_colx减1：end_rowx不用减1(源码采用for遍历取值，range()是左闭右开型)
        colx, start_rowx = self.reduceOne(colx, start_rowx)
        col_data_list = sheet_obj.col_values(colx, start_rowx=start_rowx, end_rowx=end_rowx)
        return col_data_list

    def getMaxRowNum(self, sheet_name):
        """
        :brief 获取指定sheet页的含有数据的最大行号
        :param sheet_name: sheet页名称
        :return: 返回最大行号
        """
        # 获取sheet页对象
        sheet_obj = self.wb_obj.sheet_by_name(sheet_name)
        # 获取sheet页最大的行号
        max_row_num = sheet_obj.nrows
        return max_row_num

    def getMaxColumnNum(self, sheet_name):
        """
        :brief 获取指定sheet页的含有数据的最大列号
        :param sheet_name: sheet页名称
        :return: 返回最大列号
        """
        # 获取sheet页对象
        sheet_obj = self.wb_obj.sheet_by_name(sheet_name)
        # 获取sheet页最大的列号
        max_col_num = sheet_obj.ncols
        return max_col_num

    def getSheetNames(self):

        """
        :brief 获取excel工作簿的所有sheet页名称
        :return: 以列表的形式返回excel工作簿的所有sheet页名称
        """
        sheet_name_list = self.wb_obj.sheet_names()

        return sheet_name_list

    def getCellDataType(self, sheet_name, row, col):
        """
        :brief 获取单元格的数据类型：
                   ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        :param sheet_name: sheet页名称
        :param row: 行号
        :param col:  列号
        :return: 返回单元格的数据类型
        """
        data_tpye_dict = {0: 'empty',
                          1: 'string',
                          2: 'number',
                          3: 'date',
                          4: 'boolean',
                          5: 'error'}
        # 获取sheet页对象
        sheet_obj = self.wb_obj.sheet_by_name(sheet_name)
        # 行/列值减1，保证索引号以1开始
        row, col = self.reduceOne(row, col)
        # 获取单元格值的类型，返回整型数字
        data_type_int = sheet_obj.cell(row, col).ctype
        data_tpye_str = data_tpye_dict.get(data_type_int)
        return data_tpye_str

    def getCorrectDateFormat(self, cell_val):
        """
        :brief 将xlrd读取的日期类型数据,转换为python类型的日期字符串
        :param cell_val: 单元格的数据
        :return: 返回转换后的日期字符串
        """
        date_tuple = xlrd.xldate_as_tuple(cell_val, xlrd.Book.datemode)
        year = str(date_tuple[0])
        month = str(date_tuple[1])
        day = str(date_tuple[2])
        date_str = '-'.join([year, month, day])
        return date_str


if __name__ == "__main__":
    parse_excel = ParseExcel('./excel_file/ExcelData.xlsx')
    print(parse_excel.getCell('massage', 2, 5))
    # print(parse_excel.getSheetNames())
    # print(parse_excel.getMaxRowNum('massage'))
    # print(parse_excel.getMaxColumnNum('massage'))
    # print(parse_excel.getRows('massage', 1, 1, 2))
    # print(parse_excel.getColumns('massage', 3, 1))
    if parse_excel.getCellDataType('massage', 3, 5) == 'date':
        cell_val = parse_excel.getCell('massage', 3, 5)
        print(parse_excel.getCorrectDateFormat(cell_val))
