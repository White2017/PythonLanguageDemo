# coding:utf-8  fxb_qzyx@163.com
"""
   python的闭包：
      1.形成闭包的3要素：
         1.外层函数内部定义内层函数；
         2.内层函数引用外层函数的变量；
         3.外层函数返回内层函数的引用
      2.闭包的划分：不带参数、带参数
"""


def test():
    print('无参数的test被执行！！')


def closure_out(func):
    """不传递参数的闭包"""

    def closure_in():
        func()  # 内层函数引用外层函数的变量：func

    return closure_in  # 返回内层函数的引用


def info(name, age):
    print("传递参数 >>> name:{}, age:{}".format(name, age))


def closure_out_param(func):
    """传递参数的闭包"""

    def closure_in(name, age):  # 这里接收外部传递的参数
        func(name, age)

    return closure_in


if __name__ == "__main__":
    t = closure_out(test)
    t()
    i = closure_out_param(info)
    i('jack', 20)
