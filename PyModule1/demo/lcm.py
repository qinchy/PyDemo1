# -*- coding: UTF-8 -*-

# 定义一个函数
def lcm(x, y):
    """该函数返回两个数的最小公倍数"""


    # 获取最小值
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        print("current is {0}".format(greater))
        if ((greater % x == 0) and (greater % y == 0)):
            break
        else:
            greater += 1

    return greater

if __name__ == '__main__':
    # 用户输入两个数字
    num1 = int(input("输入第一个数字: "))
    num2 = int(input("输入第二个数字: "))

    print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))
