# coding:utf-8  fxb_qzyx@163.com
import traceback

import pymongo


class MongoDB(object):
    def __init__(self, host='localhost', port=27017, database=None):
        # 创建连接对象
        self.conn_obj = pymongo.MongoClient(host=host,
                                            port=port)
        # 创建数据库对象
        self.db_obj = self.conn_obj[database]

    def insertOne(self, table_name, data_dict):
        """
        :breif 向数据库的指定表中插入数据
        :param table_name: 表名(字符串)：形如：'student'
        :param data_dict: 插入的值(字典)：形如：{'name': 'jack', 'age': 23}
        :return: None
        """
        try:
            self.table_obj = self.db_obj[table_name]
            self.table_obj.insert_one(data_dict)
            print("insert data success")
        except Exception as e:
            traceback.print_exc()

    def insertMany(self, table_name, data_list):
        """
        :breif 向数据库的指定表中插入多条数据
        :param table_name: 表名(字符串)：形如：'student'
        :param data_list: 插入的值(列表，其元素为字典格式)：形如：[{'name': 'jack'}, {'age': 23}]
        :return: None
        """
        try:
            self.table_obj = self.db_obj[table_name]
            self.table_obj.insert_many(data_list)
            print("insert many data success")
        except Exception as e:
            traceback.print_exc()

    def selectOne(self, table_name, condition=None):
        """
        :brief 按照指定条件查询表中的一条数据
        :param table_name: 表名(字符串)：形如：'student'
        :param condition: 查询的条件，字典类型,形如：{'city':wuhan}
        :return: 返回查询的结果，字典类型
        """
        try:
            self.table_obj = self.db_obj[table_name]
            # 根据查询条件查询一条数据
            data_dict = self.table_obj.find_one(condition)
            return data_dict
        except Exception as e:
            traceback.print_exc()

    def selectAll(self, table_name, condition=None):
        """
        :brief 按照指定条件查询表中的所有数据
        :param table_name: 表名(字符串)：形如：'student'
        :param condition: 查询的条件，字典类型,形如：{'city':wuhan}
        :return: 返回查询的结果，字典类型
        """
        try:
            self.table_obj = self.db_obj[table_name]
            # 根据查询条件查询满足条件的所有数据(返回cursor对象)
            cursor_obj = self.table_obj.find(condition)
            # 转换为列表
            data_dict = list(cursor_obj)
            return data_dict
        except Exception as e:
            traceback.print_exc()

    def updateOne(self, table_name, condition, update_data_dict):
        """
        :brief 按照指定条件更新表中的第一条数据
        :param table_name: 表名(字符串)：形如：'student'
        :param update_data_dict: 需要更新的数据，字典类型：形如：{'gender': True}
        :param condition: 更新的条件，字典类型,形如：{'name':'Jack'}
        :return: None
        """
        try:
            self.table_obj = self.db_obj[table_name]
            # 根据更新条件更新第一条数据:$set: 修改特定的属性值，否则会修改整个文档(即：其余的字段没有了)
            self.table_obj.update_one(condition, {"$set": update_data_dict})
            print("update one data success!")
        except Exception as e:
            traceback.print_exc()

    def updateMany(self, table_name, condition, update_data_dict):
        """
        :brief 按照指定条件更新表中所有满足条件的数据
        :param table_name: 表名(字符串)：形如：'student'
        :param condition: 更新的条件，字典类型,形如：{'name':'Jack'}
        :param update_data_dict: 需要更新的数据，字典类型：形如：{'gender': True}
        :return: None
        """
        try:
            self.table_obj = self.db_obj[table_name]
            # 根据更新条件更新第一条数据:$set: 修改特定的属性值，否则会修改整个文档(即：其余的字段没有了)
            self.table_obj.update_many(condition, {"$set": update_data_dict})
            print("update many data success!")
        except Exception as e:
            traceback.print_exc()

    def deleteOne(self, table_name, condition=None):
        """
         :brief 删除满足条件的数据集中的第一条数据
         :param table_name: 表名(字符串)：形如：'student'
         :param condition: 删除的条件，字典类型,形如：{'name':'Jack'}
         :return: None
         """
        try:
            self.table_obj = self.db_obj[table_name]
            self.table_obj.delete_one(condition)
            print("delete one data success!")
        except Exception as e:
            traceback.print_exc()

    def deleteMany(self, table_name, condition=None):
        """
         :brief 删除满足条件的数据集中的所有数据
         :param table_name: 表名(字符串)：形如：'student'
         :param condition: 删除的条件，字典类型,形如：{'name':'Jack'}
         :return: None
         """
        try:
            self.table_obj = self.db_obj[table_name]
            self.table_obj.delete_many(condition)
            print("delete many data success!")
        except Exception as e:
            traceback.print_exc()


if __name__ == "__main__":
    db = MongoDB(database='test')
    print(db.selectAll('tu', {'name': 'tom'}))
    # db.insertOne('tu', {'name': 'tom', 'age': 150})
    # db.updateOne('tu', {'name': 'tom'}, {'age': -100})
    # print(db.selectAll('tu', {'name': 'tom'}))
    # db.deleteMany('tu', {'name': 'tom'})
    print(db.selectAll('tu', {'name': 'tom'}))
