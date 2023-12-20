"""
Python 移除列表中重复的元素
"""

list_1 = [1, 2, 1, 4, 6]
# set去重了
print(list(set(list_1)))

print("删除两个列表中重复的元素")
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))

print("合并两个列表中重复的元素")
print(list(set(list_1) | set(list_2)))

print("两个列表中交集的元素")
print(list(set(list_1) & set(list_2)))