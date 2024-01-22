import datetime
from collections import namedtuple
from collections import OrderedDict


class DatePrice:
    riqi: datetime.date
    price: float

    def __init__(self, riqi: datetime.date, price: float):
        self.riqi = riqi
        self.price = price

    def __str__(self):
        print(f"riqi:{self.riqi},price:{self.price}")


def find_second_max(stock_dict):
    """计算所有价格中第二大的价格元素"""
    sorted_stock_price = sorted(zip(stock_dict.values(), stock_dict.keys()))
    return sorted_stock_price[-2]


def find_max_and_min(stock_dict):
    """计算最大值和最小值"""
    sorted_stock_price = sorted(zip(stock_dict.values(), stock_dict.keys()))
    # sorted是按升序排序的，故-1为最大值索引，0为最小值索引
    return sorted_stock_price[-1], sorted_stock_price[0]


if __name__ == '__main__':
    data_base = datetime.date(2023, 12, 31)
    price_str = '30.14,20.98,16.65,56.16'

    date_array = list()

    price_array = price_str.split(',')
    print(type(price_array))
    print(price_array)

    data_array = list()

    for idx, price in enumerate(price_array):
        currentDate = data_base + datetime.timedelta(days=idx)
        date_array.append(currentDate)

        datePrice = DatePrice(currentDate, price)
        data_array.append(datePrice)

    for datePrice in data_array:
        print("riqi=" + str(datePrice.riqi) + ",price=" + str(datePrice.price))

    # 使用zip同时迭代多个序列，构造匿名的tuple列表
    stock_tuple_list = [(riqi, price) for riqi, price in zip(date_array, price_array)]
    print(stock_tuple_list)

    # 使用命名的tuple构造列表
    stock_namedtuple = namedtuple('stock', ['riqi', 'price'])
    stock_namedtuple_list = [stock_namedtuple(riqi, price) for riqi, price in zip(date_array, price_array)]
    print(stock_namedtuple_list)
    print(f"{stock_namedtuple_list[1].riqi}的价格为{stock_namedtuple_list[1].price}")

    # 使用zip迭代成字典
    stock_dict = {riqi: price for riqi, price in zip(date_array, price_array)}
    print(stock_dict)
    print(f"20240101的价格为{stock_dict[datetime.date(2024, 1, 1)]}")

    # 使用按key排序后的字典
    stock_ordered_dict = OrderedDict((riqi, price) for riqi, price in zip(date_array, price_array))
    print(stock_ordered_dict)
    print(f"20231231的价格为{stock_ordered_dict[datetime.date(2023, 12, 31)]}")

    # 获取第二大的价格元素
    # 系统函数callable()验证是否为一个可调用的函数
    if callable(find_second_max):
        print(find_second_max(stock_ordered_dict))

    # 使用lambda表达式定义函数
    # PEP 8: E731 do not assign a lambda expression, use a def
    find_second_max_lambda = lambda stock_dict: \
        sorted(zip(stock_dict.values(), stock_dict.keys()))[-2]
    if callable(find_second_max_lambda):
        print(find_second_max_lambda(stock_ordered_dict))

    if callable(find_max_and_min):
        print(find_max_and_min(stock_ordered_dict))
