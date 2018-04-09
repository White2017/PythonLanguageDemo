# coding:utf-8  fxb_qzyx@163.com
"""
4个魔法方法的使用：类似于中间件，调用实例属性时进行拦截
   1.__getattribute__: 通过点语法(.)调用属性时，会触发
   2.__getattr__: 当通过点语法(.)调用的属性不存在时，会触发
   3.__getitem__: 通过中括号语法{[]}调用属性时，会触发
   4.__setitem__: 通过中括号语法([])给属性赋值时，会触发
"""


class Employee(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.data_dict = {}

    def __getattribute__(self, attr):
        print('__getattribute__被调用了！')
        return super().__getattribute__(attr)

    def __getattr__(self, attr):
        print('__getattr__被调用了!')
        return attr

    def __getitem__(self, attr):
        print('__getitem__被调用了！')
        return super(Employee, self).__getattribute__(attr)

    def __setitem__(self, key, value):
        print('__setitem__被调用了！ ')
        # 调用了self.data实例属性，会再次触发__getattribute__方法
        self.data_dict[key] = value


if __name__ == "__main__":
    employee = Employee('jack', 23)
    print(employee.age)  # 触发：__getattribute__
    print(employee.age1)  # 触发：__getattr__(属性age1不存在时被触发)
    print(employee['username'])  # 触发：__getitem__
    employee['salary'] = 2000  # 触发：__setitem__
