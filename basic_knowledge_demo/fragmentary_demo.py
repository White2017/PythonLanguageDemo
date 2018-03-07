# coding:utf-8


# eval()方法的使用：将字符串转换为对应的变量
def add(a, b):
    print(a + b)


add_1 = eval("add")  # 将字符串"add"转换为对应的变量,这里为add函数的引用
add_1(1, 2)  # 调用函数

if __name__ == "__main__":
    pass
