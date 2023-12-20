# -*- coding: UTF-8 -*-

import math
import cmath

def sqrt1():
    str1 = input("请输入数字:\n")
    try:
        num1 = float(str1)
    except Exception:
        raise

    return math.sqrt(num1)


def sqrt2():
    str1 = input("请输入数字:\n")
    try:
        num1 = float(str1)
    except Exception:
        raise

    return cmath.sqrt(num1)

if __name__ == '__main__':
    print("实数平方根为：{0}".format(sqrt1()))
    new_var = sqrt2()
    print("虚数平方根为：{0:0.3f}+{1:0.3f}j".format(new_var.real, new_var.imag))
