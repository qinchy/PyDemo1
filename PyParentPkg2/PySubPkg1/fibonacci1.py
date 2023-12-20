# -*- coding: UTF-8 -*-


def printFibonacci():
    before = 0
    current = 1
    count = 2

    str1 = input("请输入需要多少项:\n")

    try:
        num1 = int(str1)
    except Exception:
        print("项数必须是数字")
        raise

    if num1 < 1:
        raise Exception("项数必须大于1.")

    print(before, "\t", current, end="\t")

    while count < num1:
        newCurrent = before + current
        print("{0}".format(before + current), end="\t")
        before = current
        current = newCurrent
        count += 1


if __name__ == '__main__':
    printFibonacci()
