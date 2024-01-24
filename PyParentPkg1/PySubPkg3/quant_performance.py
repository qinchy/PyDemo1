import itertools


def __permutation():
    """
    一个列表的各种组合排列，考虑顺序
    :return:
    """
    items = [1, 2, 3]
    for item in itertools.permutations(items):
        print(item)


def __combinations():
    """
    从列表中选几个元素的选法
    :return:
    """
    items = [1, 2, 3]
    # 三选二的选法，不考虑顺序，不放回数据
    for item in itertools.combinations(items, 2):
        print(item)


def __combinations_with_replacement():
    """
    从列表中选几个元素的选法
    :return:
    """
    items = [1, 2, 3]
    # 三选二的选法，不考虑顺序，有放回顺序
    for item in itertools.combinations_with_replacement(items, 2):
        print(item)

def __product():
    """
    笛卡儿积
    :return:
    """
    items1 = [1, 2, 3]
    items2 = [4, 5]
    # 三选二的选法，不考虑顺序，有放回顺序
    for item in itertools.product(items1, items2):
        print(item)

if __name__ == '__main__':
    print("打印排列组合，考虑顺序")
    __permutation()

    print("打印几选几选法，不考虑顺序")
    __combinations()

    print("打打印几选几选法，不考虑顺序，有放回顺序")
    __combinations_with_replacement()

    print("打印笛卡尔积")
    __product()
