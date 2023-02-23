# -*- coding: UTF-8 -*-

def add():
    str1 = input("请输入数字1:\n")
    str2 = input("请输入数字2:\n")
    try:
        num1 = int(str1)
    except Exception:
        raise

    try:
        num2 = int(str2)
    except Exception:
        raise

    return num1 + num2

if __name__ == '__main__':
    print("两数之和为：{0}".format(add()))