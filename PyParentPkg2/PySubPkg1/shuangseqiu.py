# -*- coding: UTF-8 -*-
import random

def findNumber():
    # 1-33中选6个数
    red = random.sample(range(1, 33), 6)
    red.sort(reverse=False)

    # 1-16中选1个数
    blue = random.sample(range(1, 16), 1)
    print(red + blue)

if __name__ == '__main__':
    findNumber()
