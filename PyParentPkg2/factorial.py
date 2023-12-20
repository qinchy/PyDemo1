# -*- coding: UTF-8 -*-
import random

def calc():
    str1 = input("请输入要计算阶层的正整数：")

    try:
        num1 = int(str1)
    except:
        print("输入数据错误，请核查！")
        raise

    total = 1
    while num1>0:
        total = total * num1
        num1 = num1 - 1

    return total

if __name__ == '__main__':
    num = calc()
    print("计算阶层后的结果：{0}".format(num))
