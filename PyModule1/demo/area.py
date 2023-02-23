# -*- coding: UTF-8 -*-
import cmath


def calc():
    str1 = input("请输入a的值:\n")
    str2 = input("请输入b的值:\n")
    str3 = input("请输入c的值:\n")

    if str1 == '0' or str2 == '0' or str3 == '0':
        raise Exception("a、b、c不能等于0")

    try:
        num1 = int(str1)
    except Exception:
        raise

    try:
        num2 = int(str2)
    except Exception:
        raise

    try:
        num3 = int(str3)
    except Exception:
        raise

    # 计算半周长
    s = (num1 + num2 + num3) / 2

    # 计算面积
    area = (s * (s - num1) * (s - num2) * (s - num3))**0.5

    return area


if __name__ == '__main__':
    area = calc()
    print('三角形面积为 %0.2f' % area)
