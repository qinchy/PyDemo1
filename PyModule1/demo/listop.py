# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    li = ["a", "b", "mpilgrim", "z", "example"]

    # 打印第一个元素
    print(li[0])

    # 打印倒数第三个个元素
    print(li[-3])

    # 打印第1-3个元素，左闭右开
    print(li[1:3])

    # 打印第1-最后1个元素（不包括最后一个），左闭右开
    print(li[1:-1])

    # 在最后追加一个元素
    li.append("new")
    print(li[:])

    # 在第二个位置插入一个新元素
    li.insert(2, "new")
    print(li[:])

    # 在最后追加多个元素
    li.extend(["two", "elements"])
    print(li[:])

    # 搜索元素，返回下标
    print(li.index("example"))

    # 搜索不存在的元素
    try:
        li.index("c")
    except ValueError:
        print("元素不存在")

    # 删除元素
    li.remove("z")
    print(li[:])

    # 弹出最后一个元素并返回
    item = li.pop()
    print(item)

    # 两个list合并
    li = li + ['example', 'new']
    print(li[:])

    str1 = ';'.join(li)
    print(str1)

    # 过滤掉元素长度小于2的
    li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
    newlist = [elem for elem in li if len(elem) > 1]
    print("过滤掉元素长度小于2的")
    print(newlist)

    # 删除b元素
    newlist = [elem for elem in li if elem != "b"]
    print("删除b元素")
    print(newlist)

    # 查找不重复的元素
    newlist = [elem for elem in li if li.count(elem) == 1]
    print("查找不重复的元素")
    print(newlist)

    # dict
    params = {
        "server": "mpilgrim",
        "database": "master",
        "uid": "sa",
        "pwd": "secret"
    }
    # dict转list
    li2 = ["%s=%s" % (k, v) for k, v in params.items()]
    print(li2[:])
    # list转字符串
    str2 = ";".join(li2)
    # 字符串转list
    li3 = str2.split(";")
    print(li3[:])

    # dict的相关操作
    keys = params.keys()
    print(keys)
    values = params.values()
    print(values)
    item = params.items()
    print(item)

    numberList = [1, 4, 5, 7, 8, 9, 10]
    print("numberList之和为{0}".format(sum(numberList)))