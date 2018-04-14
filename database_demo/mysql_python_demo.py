# coding:utf-8  fxb_qzyx@163.com
"""
   通过使用第三方库(pymysql)来操作mysql数据库
      1.创建数据库对象，连接到指定数据库；
      2.获取cursor对象：用于执行(execute)sql语句,主要有：增删查改
      3.关闭连接：cursor连接和数据库连接
"""
import pymysql


class MysqlDB(object):
    def __init__(self,
                 host='localhost',
                 port=3306,
                 database=None,
                 user=None,
                 password=None):
        # 创建数据库对象，连接到指定的数据库
        self.conn_obj = pymysql.Connection(host=host,
                                           port=port,
                                           database=database,
                                           user=user,
                                           password=password,
                                           charset='utf8')

        # 获取cursor对象，用于执行sql语句
        self.cursor_obj = self.conn_obj.cursor()

    def insert(self, table_name, field, value):
        """
        :brief 向数据库的指定表中插入数据, 形如："student", "(name, age)", "('jack', 20)"
        :param table_name: 表名,形如："student"
        :param field: 表的字段名,形如："(name, age)"
        :param value: 插入的值, 形如："('jack', 20)"
        :return: None
        """
        insert_sql = "insert into {table_name}{field} values{value}".format(
            table_name=table_name,
            field=field,
            value=value)
        print(insert_sql)

        try:
            # 执行sql语句
            self.cursor_obj.execute(insert_sql)
            # 提交到数据库执行
            self.conn_obj.commit()
            print("insert data success")
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.conn_obj.rollback()

    def update(self, table_name, updated_value, condition=None):
        """
        :brief 更新表中某一条/多条数据中相关字段的值
        :param table_name: 表名，形如："student"
        :param updated_value: 要更新的字段，形如："name= 'Tom', City = 'Nanjing'"
        :param condition: 查询的条件，形如："id=5" 或  "country = 'China'"
        :return: None
        """
        if not condition:  # 若更新条件为空，则会很危险，需终止更新
            print("update condition can't empty")
            return
        update_sql = "update {table_name} set {updated_value} where {condition}".format(
            table_name=table_name,
            updated_value=updated_value,
            condition=condition)

        try:
            # 执行sql语句
            self.cursor_obj.execute(update_sql)
            # 提交到数据库执行
            self.conn_obj.commit()
            print("update data success")
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.conn_obj.rollback()

    def delete(self, table_name, condition):
        """
        :brief 根据条件，删除表中的某些数据
        :param table_name: 表名，形如："student"
        :param condition: 查询的条件，形如："id>5" 或  "country = 'China'"
        :return: None
        """
        delete_sql = "delete from {table_name} where {condition}".format(
            table_name=table_name,
            condition=condition)

        try:
            # 执行sql语句
            self.cursor_obj.execute(delete_sql)
            # 提交到数据库执行
            self.conn_obj.commit()
            print("delete data success")
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.conn_obj.rollback()

    def fetchall(self, table_name, field, condition=None):
        """
        :breif 查询数据
        :param table_name: 表名，形如："student"
        :param field: 需要查询的字段,形如："name, age"
        :param condition: 查询的条件，形如：
        :return: 返回查询到的结果(元组)
        """
        select_sql = "select {field} from {table_name} where {condition}".format(
            field=field,
            table_name=table_name,
            condition=condition)

        if not condition:  # 查询条件为空时，执行该语句,全部查询
            select_sql = "select {field} from {table_name}".format(
                field=field,
                table_name=table_name)

        try:
            # 执行sql语句
            self.cursor_obj.execute(select_sql)
            # 提交到数据库执行,返回的结果为元组
            result_tuple = self.cursor_obj.fetchall()
            print("select data success")
            return result_tuple
        except Exception as e:
            print(e)

    def close(self):
        """
        :brief 关闭连接
        :return: None
        """
        # 关闭cursor对象
        self.cursor_obj.close()
        # 关闭数据库连接对象
        self.conn_obj.close()


if __name__ == "__main__":
    db_obj = MysqlDB(database='test', user='root', password='mysql')
    # result = db_obj.fetchall('student', 'name, age, country', 'id>2')
    # print(result)
    # db_obj.insert('student', '(name, age)', "('LiSi', 22)")
    # db_obj.update('student', "name='xiaoming'", "id=5")
    # db_obj.delete('student', "id=5")
    db_obj.close()
