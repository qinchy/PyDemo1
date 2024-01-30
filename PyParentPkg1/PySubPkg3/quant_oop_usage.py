import itertools
from abc import ABCMeta, abstractmethod
from collections import namedtuple, OrderedDict
from collections.abc import Iterable
from concurrent.futures import ProcessPoolExecutor
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

    def __init_change(self):
        """
        从price_array生成change_array
        :return:
        """
        price_float_array = [float(price_str) for price_str in self.__price_array]
        # 通过讲时间平移形成两个错开的收盘价序列，通过zip()函数打包成为一个新的序列
        # 每个元素为响铃的两个收盘价格
        pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]
        change_array = map(lambda pp: reduce(lambda price1, price2: round((price2 - price1) / price1, 3), pp), pp_array)
        change_array_list = list(change_array)
        # 第一天涨幅设置为0
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
        # getter函数
        return self.__buy_change_threshold

    @buy_change_threshold.setter
    def buy_change_threshold(self, buy_change_threshold):
        if not isinstance(buy_change_threshold, float):
            """
            上涨阈值只取小数点后两位
            """
            raise TypeError('buy_change_threshold must be float!')
        self.__buy_change_threshold = round(buy_change_threshold, 2)


class TradeStrategy2(TradeStrategyBase):
    """
    交易策略2：均值恢复策略，当股价连续两个交易日下跌
    且下跌幅度超过阈值默认s_buy_change_threshold(-10%),
    买入股票并持有s_stock_change_threshold(10)天
    """
    # 买入后持有天数
    s_keep_stock_threshold = 10
    # 下跌买入阈值
    s_buy_change_threshold = -0.10

    def __init__(self):
        self.keep_stock_day = 0

    def buy_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_ind >= 1:
            """
            当没有持有股票的时候self.keep_stock_day ==0 并且
            trade_ind>=1,不是交易开似乎的第一天，因为需要yesterday数据
            """
        # trade_day.change<0 bool:今天股价是否下跌
        today_down = trade_day.change < 0
        yesterday_down = trade_days[trade_ind - 1].change < 0
        # 两天总跌幅
        down_rate = trade_day.change + \
                    trade_days[trade_ind - 1].change
        if today_down and yesterday_down and down_rate < TradeStrategy2.s_buy_change_threshold:
            # 买入条件成立，连跌两天，跌幅超过s_buy_change_threshold
            self.keep_stock_day += 1
        elif self.keep_stock_day > 0:
            # self.keep_stock_day>0代表持有股票。持有股票天数递增
            self.keep_stock_day += 1

    def sell_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day >= TradeStrategy2.s_keep_stock_threshold:
            # 当持有股票太难书超过阈值s_keep_stock_threshold
            self.keep_stock_day = 0

    """
    类方法，不需要self参数，但第一个参数需要是标识自身类的cls参数
    """

    @classmethod
    def set_keep_stock_threshold(cls, keep_stock_threshold):
        cls.s_keep_stock_threshold = keep_stock_threshold

    """
    静态方法，只能通过直接类名.属性名或类名.方法名调用类中的变量和方法
    """

    @staticmethod
    def set_buy_change_threshold(buy_change_threshold):
        TradeStrategy2.s_buy_change_threshold = buy_change_threshold


class TradeLoopBack(object):
    """
    交易回测系统
    """

    def __init__(self, trade_days, trade_strategy):
        """
        使用前面疯转的StockTradeDays类和本章节编写的交易策略类TradeStrategyBase类初始化交易系统
        :param trade_days:
        :param trade_strategy:
        """
        self.trade_days = trade_days
        self.trade_strategy = trade_strategy
        # 交易盈亏结果序列
        self.profit_array = []

    def execute_trade(self):
        """
        执行交易回测
        """
        for ind, day in enumerate(self.trade_days):
            """
            以时间驱动完成交易回测
            """
            if self.trade_strategy.keep_stock_day > 0:
                # 如果持有股票，加入交易盈亏结果序列
                self.profit_array.append(day.change)

            # hasattr:用来查询对象有没有实现某个方法
            if hasattr(self.trade_strategy, 'buy_strategy'):
                # 买入策略执行
                self.trade_strategy.buy_strategy(ind, day, self.trade_days)

            # hasattr:用来查询对象有没有实现某个方法
            if hasattr(self.trade_strategy, 'sell_strategy'):
                # 买入策略执行
                self.trade_strategy.sell_strategy(ind, day, self.trade_days)


def calc(trade_days, keep_stock_threshold, buy_change_threshold):
    """

    :param keep_stock_threshold:持股天数
    :param buy_change_threshold:下跌买入阈值
    :return:
    """
    # 实例化交易策略
    trade_strategy2 = TradeStrategy2()
    # 通过类方法设置买入后持股天数
    TradeStrategy2.set_keep_stock_threshold(keep_stock_threshold)
    # 通过静态方法设置下跌买入阈值
    TradeStrategy2.set_buy_change_threshold(buy_change_threshold)

    # 进行回测
    trade_loop_back = TradeLoopBack(trade_days, trade_strategy2)

    trade_loop_back.execute_trade()
    # 计算回测结果的最终盈亏值profit
    profit = 0.0 if len(trade_loop_back.profit_array) == 0 else \
        reduce(lambda a, b: a + b, trade_loop_back.profit_array)
    return profit, keep_stock_threshold, buy_change_threshold


result = []


# 回调函数
def when_done(r):
    """多线程时回调函数，通过add_done_callback任务完成后调用"""
    result.append(r.result())


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

    stockdata, change_sum = trade_days.filter_stock(want_up=False, want_calc_sum=True)
    print(f'过滤后的数据：{stockdata}, 累计涨跌：{change_sum}')

    """
    后面执行回测
    """

    """
    追涨模式
    """
    trade_loop_back = TradeLoopBack(trade_days, TradeStrategy1())
    trade_loop_back.execute_trade()
    print('回测策略1总盈亏:{}%'.format(reduce(lambda a, b: a + b, trade_loop_back.profit_array) * 100))

    """
    价值回归模式
    """
    trade_strategy2 = TradeStrategy2();
    trade_loop_back = TradeLoopBack(trade_days, trade_strategy2)
    trade_loop_back.execute_trade()
    print('回测策略2总盈亏:{}%'.format(reduce(lambda a, b: a + b, trade_loop_back.profit_array) * 100))

    # 下跌20%后买入，持有20天
    TradeStrategy2.set_buy_change_threshold(float(-0.20))
    TradeStrategy2.set_keep_stock_threshold(20)
    trade_loop_back.execute_trade()
    print('回测策略3总盈亏:{}%'.format(reduce(lambda a, b: a + b, trade_loop_back.profit_array) * 100))

    # 计算最佳盈利及其持股天数和下跌买入阈值
    print("计算最佳盈利及其持股天数和下跌买入阈值")
    profit, keep_stock_threshold, buy_change_threshold = calc(trade_days, 20, -0.08)
    print(f'盈利：{profit},持股天数：{keep_stock_threshold}，下跌买入阈值：{buy_change_threshold}')

    # 使用多个持股天数与下跌买入阈值的笛卡尔积来寻求最佳盈利参数
    # range集合，买入后持股天数从2~30天，间隔2天
    keep_stock_days_list = range(2, 30, 2)
    # 下跌买入阈值从-5%到-15%
    buy_change_list = [buy_change / 100.0 for buy_change in range(-5, -16, -1)]
    # 存放各种场景的收益数据、持股天数，下跌买入阈值
    result = []
    for keep_stock_threshold, buy_change_threshold in itertools.product(keep_stock_days_list, buy_change_list):
        print(f"持股天数：{keep_stock_threshold}，下跌买入阈值：{buy_change_threshold}")
        result.append(calc(trade_days, keep_stock_threshold, buy_change_threshold))
    print(f"笛卡尔积参数集合总共结果为：{len(result)}个")
    print(result)
    # [::-1]将整个结果反转，反转后盈亏收益从最高向低开始排序
    # [:10]取出收益最高的前10个组合
    high_profit = sorted(result)[::-1][:10]
    print("收益最高的10个组合如下")
    for profit, days, change in high_profit:
        print(f'收益率：{profit},持股天数：{days},下跌幅度：{change}')

    print("==================多进程处理  BEGIN==================")

    # range集合，买入后持股天数从2~30天，间隔2天
    keep_stock_days_list = range(2, 30, 2)
    # 下跌买入阈值从-5%到-15%
    buy_change_list = [buy_change / 100.0 for buy_change in range(-5, -16, -1)]
    with ProcessPoolExecutor() as pool:
        for keep_stock_threshold, buy_change_threshold in itertools.product(keep_stock_days_list, buy_change_list):
            print(f"持股天数：{keep_stock_threshold}，下跌买入阈值：{buy_change_threshold}")
            future_result = pool.submit(calc, trade_days, keep_stock_threshold, buy_change_threshold)
            future_result.add_done_callback(when_done)
    print(result)
    # [::-1]将整个结果反转，反转后盈亏收益从最高向低开始排序
    # [:10]取出收益最高的前10个组合
    high_profit = sorted(result)[::-1][:10]
    print("收益最高的10个组合如下")
    for profit, days, change in high_profit:
        print(f'收益率：{profit},持股天数：{days},下跌幅度：{change}')

    print("====================多进程处理 END====================")
