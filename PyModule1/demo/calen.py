# -*- coding: UTF-8 -*-

import calendar
"""该函数返回两个数的之和"""
if __name__ == '__main__':
    # 输入指定年月
    yy = int(input("输入年份: "))
    mm = int(input("输入月份: "))

    # 显示日历
    print(calendar.month(yy, mm))
    monthRange = calendar.monthrange(yy, mm)
    print("{0}年{1}月有{2}天，第一天是星期{3}".format(yy, mm, monthRange[1],
                                           monthRange[0] + 1))
