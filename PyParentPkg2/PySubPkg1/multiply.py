# -*- coding: UTF-8 -*-

def printMultiply():
    for i in range(1, 10):
        j = 1
        while j <= i:
            print("{0}*{1}={2}".format(j, i, i * j), end="\t")
            if j == i:
                print(end="\n")
            j = j + 1


if __name__ == '__main__':
    printMultiply()
