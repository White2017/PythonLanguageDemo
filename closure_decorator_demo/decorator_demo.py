# coding:utf-8  fxb_qzyx@163.com
"""
python的装饰器：本质上是利用了闭包的原理
   1.装饰器的使用：
        1.定义闭包函数
        2.将该闭包函数作用于被装饰的对象上
"""


# 定义闭包函数,用作装饰器(作用在函数上的装饰器，且装饰器本身不带参数)
def closure_out_param(func):
    """传递参数的闭包"""

    def closure_in(name, age):  # 这里接收外部传递的参数
        func(name, age)

    return closure_in


@closure_out_param
def info(name, age):
    print("传递参数 >>> name:{}, age:{}".format(name, age))


if __name__ == "__main__":
    info('jack', 20)
