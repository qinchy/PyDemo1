#!/usr/bin/python3
import random

if __name__ == '__main__':
    random.seed()
    print("使用默认种子生成随机数：", random.random())
    print("使用默认种子生成随机数：", random.random())

    random.seed(10)
    print("使用整数 10 种子生成随机数：", random.random())
    random.seed(10)
    print("使用整数 10 种子生成随机数：", random.random())

    random.seed("hello", 2)
    print("使用字符串种子生成随机数：", random.random())
