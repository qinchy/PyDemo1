"""
@param str1 原字符串
@paramnum 要移除的位置
@return 移除后的字符串
"""


def ff(str1, num):
    return str1[:num] + str1[num + 1:]


if __name__ == "__main__":
    str1 = 'Runoob'
    print(ff(str1, 2))
    print(ff(str1, 4))
