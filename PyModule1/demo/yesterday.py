# -*- coding: UTF-8 -*-

import datetime


def getYesterday(yy, mm, dd):
    today = datetime.datetime(yy, mm, dd)
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

if __name__ == "__main__":
    yy = int(input("输入年: "))
    mm = int(input("输入月: "))
    dd = int(input("输入日: "))

    yesterday = getYesterday(yy, mm, dd)
    print(yesterday)
