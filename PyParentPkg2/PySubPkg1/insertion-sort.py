"""
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
https://www.runoob.com/python3/python-insertion-sort.html
"""


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            # 如果后一个比前一个小，则把大的值往后移动一位。
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':

    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print("排序后的数组:")
    for i in range(len(arr)):
        print("%d" % arr[i])
