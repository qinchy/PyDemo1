import numpy as np

if __name__ == '__main__':
    # 股票数量
    stock_count = 200
    # 504个交易日
    view_days = 504

    # 生成服从正太分布：均值期望=0，标准差=1的序列
    stock_day_change = np.random.standard_normal((stock_count, view_days))
    print(stock_day_change.shape)

    # 打印第一支股票，前5个交易日的涨跌幅情况
    print(stock_day_change[0:1, :5])
