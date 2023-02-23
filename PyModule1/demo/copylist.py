def clone_runoob1(li1):
    li_copy = li1[:]
    return li_copy


def clone_runoob2(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


def clone_runoob3(li1):
    li_copy = list(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
print("原始列表:", li1)

print("使用截取方式复制")
li2 = clone_runoob1(li1)
print("复制后列表:", li2)

print("使用extend方式复制")
li2 = clone_runoob2(li1)
print("复制后列表:", li2)

print("使用构造函数list方式复制")
li2 = clone_runoob3(li1)
print("复制后列表:", li2)
