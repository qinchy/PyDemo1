from abc import ABCMeta, abstractmethod
from collections import namedtuple, OrderedDict
from collections.abc import Iterable
from functools import reduce

import six


class StockTradeDays(object):
    """
    股票交易数据类定义
    """

    def __init__(self, price_array, start_date, date_array=None):
        # 私有价格序列
        self.__price_array = price_array
        # 私有日期序列
        self.__date_array = self._init_days(start_date, date_array)
        # 私有涨跌幅序列
        self.__change_array = self.__init_change()
        # 进行OrderedDict组装
        self.stock_dict = self.__init_stock_dict()

    def __init_change(self):
        """
        从price_array生成change_array
        :return:
        """
        price_float_array = [float(price_str) for price_str in self.__price_array]
        # 通过讲时间平移形成两个错开的收盘价序列，通过zip()函数打包成为一个新的序列
        # 每个元素为响铃的两个收盘价格
        pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]
        change_array = map(lambda pp: reduce(lambda a, b: round((b - a) / a, 3), pp), pp_array)
        change_array_list = list(change_array)
        change_array_list.insert(0, 0)

        return change_array_list

    def __init_stock_dict(self):
        """
        使用namedtuple，OrderdDict将结果合并
        :return:
        """
        stock_namedtuple = namedtuple('stock', ('date', 'price', 'change'))
        stock_dict = OrderedDict((date, stock_namedtuple(date, price, change)) for date, price, change in
                                 zip(self.__date_array, self.__price_array, self.__change_array))
        return stock_dict

    def _init_days(self, start_date, date_array):
        """
        protect方法，初始化交易日期序列
        :param start_date:初始日期
        :param date_array:给定日期序列
        :return:
        """
        if date_array is None:
            # 由start_date和self.__price_array来确定日期序列
            date_array = [str(start_date + ind) for ind, _ in enumerate(self.__price_array)]
        else:
            # 稍后的内容会使用外部直接设置的方式
            date_array = [str(date) for date in date_array]
        return date_array

    def filter_stock(self, want_up=True, want_calc_sum=False):
        """
        筛选结果数据
        :param self:
        :param want_up:是否筛选上涨
        :param want_calc_sum: 是否计算涨跌幅和
        :return:
        """
        filter_func = (lambda day: day.change > 0) if want_up else (lambda day: day.change < 0)
        # 使用filter_func作为筛选函数
        want_days = filter(filter_func, self.stock_dict.values())
        if not want_calc_sum:
            return list(want_days), 0

        # 需要计算涨跌幅和
        change_sum = 0.0
        days = list()
        for day in want_days:
            change_sum += day.change
            days.append(day)
        return days, change_sum

    def __str__(self):
        return str(self.stock_dict)

    __repr__ = __str__

    def __iter__(self):
        """
        通过代理stock_dict的迭代，yield元素
        :param self:
        :return:
        """
        for key in self.stock_dict:
            yield self.stock_dict[key]

    def __getitem__(self, ind):
        """
        获取索引的元素项
        :param ind:
        :return:
        """
        date_key = self.__date_array[ind]
        return self.stock_dict[date_key]

    def __len__(self):
        return len(self.stock_dict)


class TradeStrategyBase(six.with_metaclass(ABCMeta, object)):
    """
    交易策略抽象基类
    """

    @abstractmethod
    def buy_strategy(self, *args, **kwargs):
        """
        买入策略实现
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def sell_strategy(self, *args, **kwargs):
        """
        卖出策略
        :param args:
        :param kwargs:
        :return:
        """
        pass


class TradeStrategy1(TradeStrategyBase):
    """
    交易策略1：追涨策略，当股价上涨一个阈值默认为7%时
    买入股票并持有s_keep_stock_threshold(20)天
    """
    s_keep_stock_threshold = 20

    def __init__(self):
        self.keep_stock_day = 0
        self.__buy_change_threshold = 0.07

    def buy_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day == 0 and \
                trade_day.change > self.__buy_change_threshold:
            # 当没有持有股票的时候self.keep_stock_day==0 并且
            # 符合买入条件上涨一个阈值，买入
            self.keep_stock_day += 1

        elif self.keep_stock_day > 0:
            # self.keep_stock_day>0代表持有股票，持有股票天数递增
            self.keep_stock_day += 1

    def sell_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day >= \
                TradeStrategy1.s_keep_stock_threshold:
            # 当持有股票天数超过阈值s_keep_stock_threshold，卖出股票
            self.keep_stock_day = 0

    """
    property属性
    """

    @property
    def buy_change_threshold(self):
        return self.__buy_change_threshold

    @buy_change_threshold.setter
    def buy_change_threshold(self, buy_change_threshold):
        if not isinstance(buy_change_threshold, float)
            """
            上涨阈值只取小数点后两位
            """
            raise TypeError('buy_change_threshold must be float!')
        self.__buy_change_threshold = round(buy_change_threshold, 2)


if __name__ == '__main__':
    price_array = '30.14,29.58,26.36,32.56,32.82'.split(',')
    date_base = 20240101

    # 从StockTradeDays类初始化一个实例对象trade_days，内部会调用__init__
    trade_days = StockTradeDays(price_array, date_base)

    print(trade_days)
    print(f'trade_days对象长度为{len(trade_days)}')

    # 迭代遍列
    if isinstance(trade_days, Iterable):
        for day in trade_days:
            print(day)

    stock, change_sum = trade_days.filter_stock(want_up=False, want_calc_sum=True)
    print(f'过滤后的数据：{stock}, 累计涨跌：{change_sum}')
