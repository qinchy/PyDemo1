import datetime
from collections import namedtuple
from collections import OrderedDict
from functools import reduce


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


def calc_increase_percent(stock_dict):
    """通过收盘价计算每天涨跌幅"""
    # 将字符串的价格通过列表推导式显式转换为float类型
    # 由于stock_dict是OrderedDict，所以才可以直接使用stock_dict.values()获取有序日期的收盘价格
    price_float_list = [float(price_str) for price_str in stock_dict.values()]
    open_close_price_tuple_list = [(openPrice, closePrice) for openPrice, closePrice in
                                   zip(price_float_list[:-1], price_float_list[1:])]
    print(open_close_price_tuple_list)
    # 普通写法
    for (openPrice, closePrice) in open_close_price_tuple_list:
        increse = str(round((closePrice - openPrice) / openPrice, 3) * 100) + "%"
        print(f"{openPrice} -> {closePrice}, 上涨了{increse}")

    # 用map，reduce高阶写法代替上面普通写法
    increase_list = map(
        lambda open_close_price_tuple: reduce(lambda a, b: round((b - a) / a, 3), open_close_price_tuple),
        open_close_price_tuple_list)
    # 这里得用list包装一下再打印，否则打印出内存地址
    full_increase_list = list(increase_list)
    full_increase_list.insert(0, 0)
    print(full_increase_list)

    stock_namedtuple = namedtuple('stock', ('riqi', 'price', 'increase'))
    stock_dict_new = OrderedDict((riqi, stock_namedtuple(riqi, price, increase)) for riqi, price, increase in
                                 zip(stock_dict.keys(), price_float_list, full_increase_list))
    print(stock_dict_new)
    for value in stock_dict_new.values():
        print(value.increase)
    print("过滤下跌的股票数据后：")
    data = list(filter(lambda value: value.increase > 0, stock_dict_new.values()))
    print(data)

    # 也可以调用函数实现，只保留上涨，不计算累计
    print("只保留上涨，不计算累计")
    data1, increase_sum = filter_stock(stock_dict_new)
    print(data1)
    print(increase_sum)

    # 也可以调用函数实现，只保留下跌，不计算累计
    print("只保留下跌，不计算累计")
    data2, increase_sum = filter_stock(stock_dict_new, want_up=False)
    print(data2)
    print(increase_sum)

    # 也可以调用函数实现，只保留下跌，不计算累计
    print("只保留下跌，要计算累计")
    data3, increase_sum = filter_stock(stock_dict_new, want_up=False, want_calc_sum=True)
    print(data3)
    print(increase_sum)


def filter_stock(stock_array_dict, want_up=True, want_calc_sum=False):
    """根据条件过滤数据"""
    if not isinstance(stock_array_dict, OrderedDict):
        raise TypeError('stock_array_dict must be OrderedDict!')

    filter_func = (lambda stock: stock.increase > 0) \
        if want_up else (lambda stock: stock.increase < 0)
    want_stock_data = filter(filter_func, stock_array_dict.values())

    if not want_calc_sum:
        return list(want_stock_data), 0

    # 需要计算涨跌幅和
    increase_sum = 0.0
    dest = list()
    for stock in want_stock_data:
        # want_stock_data貌似只能消费一次
        increase_sum += stock.increase
        dest.append(stock)
    return dest, increase_sum


def calc_square():
    """使用 lambda 匿名函数计算平方数"""
    square = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
    print(square, list(square))


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

    # 找最大最小收盘价
    if callable(find_max_and_min):
        print(find_max_and_min(stock_ordered_dict))

    # 计算上涨百分比
    if callable(calc_increase_percent):
        calc_increase_percent(stock_ordered_dict)

    # 计算平方
    if callable(calc_square):
        calc_square()
