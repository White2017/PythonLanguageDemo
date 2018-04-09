# coding:utf-8  fxb_qzyx@163.com
"""
   单例模式：通过__new__方法实现
"""


class SingletonDemo(object):
    """单例模式：用在多线程中，会出现bug，需要使用Lock"""
    # 定义类变量：用于存储__new__实例化的对象
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 若__instance为None则赋值为对象本身,否则返回之前的对象，从而保证为同一个
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, test_name):
        self.test_name = test_name


if __name__ == "__main__":
    # 创建3个实例，并传入test_name
    singleton_1 = SingletonDemo('singleton_1')
    singleton_2 = SingletonDemo('singleton_2')
    singleton_3 = SingletonDemo('singleton_3')
    # 打印实例的id值, 均相同
    print("singleton_1's id >>> ", id(singleton_1))
    print("singleton_2's id >>> ", id(singleton_2))
    print("singleton_3's id >>> ", id(singleton_3))
    # 打印实例的test_name，均为：singleton_3,
    print(singleton_1.test_name)  # singleton_3
    print(singleton_2.test_name)  # singleton_3
    print(singleton_3.test_name)  # singleton_3
