#!/usr/bin/python3

import sys

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __del__(self):
        print(f"Vector({self.a},{self.b})已被删除")

    def param(self, *args, **kwargs):
        print(self)

        print(type(args))
        for arg in args:
            self.a = self.a + arg

        print(self)

        print(type(kwargs))
        for kwarg in kwargs:
            print(kwarg)


if __name__ == '__main__':
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)

    v1.param(1, 2, 3, 4, 5, a="a", b="b")
    v1.param(1, 2, 3, 4, 5, c="c", d="d")

    # +号会调用Vector的__add__方法
    # print会调用__str__方法
    print(v1 + v2)

    print(type(sys.addaudithook))
