# -*- coding: UTF-8 -*-
import cmath


def calc():
    str1 = input("请输入a的值:\n")
    str2 = input("请输入b的值:\n")
    str3 = input("请输入c的值:\n")

    if str1 == 0:
        raise Exception("a不能等于0")

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

    # 计算
    d = (num2**2) - (4 * num1 * num3)

    # 两种求解方式
    sol1 = (-num2 - cmath.sqrt(d)) / (2 * num1)
    sol2 = (-num2 + cmath.sqrt(d)) / (2 * num1)

    return sol1, sol2


if __name__ == '__main__':
    sol1, sol2 = calc()
    print('结果为 {0} 和 {1}'.format(sol1, sol2))
