# coding:utf-8  fxb_qzyx@163.com
"""
   快速排序的python实现！
      思想：
          1.找基准：从序列中找一个元素作为基准；
          2.分区操作：将序列中比基准小的数放在基准左边，比基准大的数放在基准右边
          3.递归：把小于基准值元素的子序列和大于基准值的子序列进行递归(即重复步骤2的操作)
"""


def quick_sort(data_list, start, end):
    """
    :brief 快速排序，将列表中的数字按从小到大的顺序排序(时间复杂度:o(nlog(n)))
    :param data_list: 需要排序的列表
    :param start: 列表的起始索引号
    :param end: 列表的结束索引号
    :return: None
    """
    if start >= end:  # 当起始索引不小于结束索引时，结束递归
        return
    # 设定基准值为起始元素
    base_val = data_list[start]
    # left：由左向右移动的游标
    left = start
    # right：有右向左移动的游标
    right = end
    while left < right:
        # 若左右游标未重合，且 右边游标元素不比基准元素小，则右边游标向左移动
        while left < right and data_list[right] >= base_val:
            right -= 1

        # 条件不满足，则退出循环，将右侧元素赋值给左侧
        data_list[left] = data_list[right]

        # 若左右游标未重合，且 左边游标元素不比基准元素大，则左边游标向右移动
        while left < right and data_list[left] < base_val:
            left += 1

        # 条件不满足，则退出循环，将左侧元素赋值给右侧
        data_list[right] = data_list[left]

    # 退出循环后，left与right重合，此时的位置为基准元素应当在的正确位置，将基准元素放到该位置
    data_list[right] = base_val

    # 将基准元素左右两侧的子序列再次进行递归排序
    quick_sort(data_list, start, left - 1)
    quick_sort(data_list, left + 1, end)


if __name__ == "__main__":
    data_list = [4, 3, 2, 6, 7, 1]
    quick_sort(data_list, 0, len(data_list) - 1)
    print(data_list)
