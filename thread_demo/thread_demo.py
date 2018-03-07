# coding:utf-8
"""
    通过threading模块的Thread类来创建线程对象
"""
import threading
import time


def worker():
    print("working...")
    time.sleep(2)
    print("finished!!")


t1 = threading.Thread(target=worker, name="worker")
t1.start()

print("主线程结束！！")

if __name__ == "__main__":
    pass
