def check1(string, sub_str):
    if string.find(sub_str) == -1:
        print("不存在！")
    else:
        print("存在！")


def check2(string, sub_str):
    if sub_str in string:
        print('存在')
    else:
        print('不存在')


if __name__ == '__main__':
    string = "www.runoob.com"
    sub_str = "runoob"

    print("用find方式")
    check1(string, sub_str)

    print("用in方式")
    check2(string, sub_str)
