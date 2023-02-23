from functools import reduce


def returnSum2(dict: dict):
    return reduce(lambda x, y: x + y, dict.values())


def returnSum1(myDict: dict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum


def returnSum3(myDict: dict):
    return sum(myDict.values())


if __name__ == '__main__':
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum :", returnSum1(dict))
    print("Sum :", returnSum2(dict))
    print("Sum :", returnSum3(dict))
