# -*- coding: UTF-8 -*-


def printArmstrong():
    str1 = input("请输入要判断是否为阿姆斯特朗数的数:\n")

    try:
        num1 = int(str1)
    except Exception:
        print("输入的数必须是数字")
        raise

    if num1 < 1:
        raise Exception("输入的数必须大于1.")

    length = len(str1)

    sum = 0
    temp = num1

    while temp > 0:
        digit = temp % 10
        sum += digit**length
        temp //= 10

    # 输出结果
    if num1 == sum:
        print(str1, "是阿姆斯特朗数")
    else:
        print(str1, "不是阿姆斯特朗数")


if __name__ == '__main__':
    printArmstrong()
