def merge1(src: dict, dest: dict) -> dict:
    return dest.update(src)


def merge2(src: dict, dest: dict) -> dict:
    res = {**src, **dest}
    return res


if __name__ == '__main__':
    # 两个字典
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    merge1(dict1, dict2)
    print(dict2)

    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    mergedDict = merge2(dict1, dict2)
    print(mergedDict)
