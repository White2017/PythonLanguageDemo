# coding:utf-8
"""
    通过threading模块的Thread类来创建线程对象,传递参数
"""
import threading
import time
import random


def worker(name, employee_id):
    print("{id} {name} is working...".format(name=name, id=employee_id))
    random_time = random.randint(3, 5)
    time.sleep(random_time)
    print("{id} {name}'s work finished!!".format(name=name, id=employee_id))


for employee_id in range(1, 11):
    employee_name = "-".join(['jack', str(employee_id)])
    # 线程的传参
    t = threading.Thread(target=worker, args=(employee_name, employee_id))
    t.start()

if __name__ == "__main__":
    pass
