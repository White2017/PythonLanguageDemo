# coding:utf-8  fxb_qzyx@163.com
"""
   冒泡排序的python实现:相邻元素两两比较，反序则交换
        eg:5,4,3,2,1
           4,3,2,1,5    <---- one
           3,2,1,4,5    <---- two
           2,1,3,4,5    <---- three
           1,2,3,4,5    <---- four

"""


def bubble_sort(data_list):
    """
    :brief :冒泡排序，将列表中的数字按从小到大的顺序排序(最优时间复杂度：O(n))
    :param data_list: 需要排序的列表
    :return: None
    """
    data_list_len = len(data_list)
    flag = True  # 标记，若值为true,则表示本次循环没有值进行交换，为有序状态，排序完成了
    for i in range(data_list_len - 1, 0, -1):
        # i表示每次遍历需要比较的次数：n/n-1/n-2/n-3....3/2/1
        for j in range(i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                flag = False
        if flag:
            break


if __name__ == "__main__":
    data_list = [5, 4, 3, 2, 1]
    # data_list = [1, 2, 3, 4, 5]
    bubble_sort(data_list)
    print(data_list)
