# coding:utf-8  fxb_qzyx@163.com
"""
   选择排序的python实现:
          首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
      再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推
"""


def selection_sort(data_list):
    """
    :brief :选择排序，将列表中的数字按从小到大的顺序排序(时间复杂度：O(n^2))
    :param data_list: 需要排序的列表
    :return: None
    """
    data_list_len = len(data_list)

    for i in range(data_list_len):  # 外层循环：需要查找的次数
        index = i  # 假定起始的索引号为最值的索引号
        for j in range(i + 1, data_list_len):  # 找到最值的索引号
            if data_list[index] > data_list[j]:
                index = j

        if index != i:  # 若不是假定的最值，则交换结果
            data_list[i], data_list[index] = data_list[index], data_list[i]


if __name__ == "__main__":
    data_list = [5, 4, 3, 2, 1, 6, 7, 4]
    selection_sort(data_list)
    print(data_list)
