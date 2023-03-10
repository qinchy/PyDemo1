#!/usr/bin/python3

import calendar
import time  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(ticks)
print("本地时间为 :", localtime)

# 格式化本地时间，1.传入time.struct_time类型
localtimestr1 = time.asctime(localtime)
print("本地时间为 :", localtimestr1)

# 格式化本地时间，2.传入Tuple元组
localtimestr2 = time.asctime((2023, 3, 10, 10, 4, 46, 4, 69, 0))
print("本地时间为 :", localtimestr2)

# 元组->时间戳
timestamp1 = calendar.timegm((2023, 3, 10, 10, 4, 46, 4, 69, 0))
print(timestamp1)

# 时间戳->元组
print(time.gmtime(timestamp1))

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", localtime))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print(time.perf_counter())  # 返回系统运行时间
print(time.process_time())  # 返回进程运行时间

# 日历
cal = calendar.month(2023, 3)
print("以下输出2023年3月份的日历:")
print(cal)

# 相当于 print(calendar.month(theyear, themonth, w=0, l=0))。
calendar.prmonth(2023, 3, w=0, l=0)
print("---------------------------------------")

# 返回一个多行字符串格式的 year 年年历，m 是每行几个月。 c 是每月间隔宽度。 w 是每日间隔宽度。 l 是每星期行数。
print(calendar.calendar(2023, w=2, l=1, c=6, m=3))

# 相当于 print (calendar.calendar(year, w=0, l=0, c=6, m=3))。
calendar.prcal(2023, w=0, l=0, c=6, m=3)
print("===========================================")

# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
# [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 0, 0]]
print(calendar.monthcalendar(2023, 3))

# 返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0（星期一）到 6（星期日）。
# (2, 31)  -> 2 表示 2023 年 3 月份的第一天是周三，31 表示 2023 年 3 月份总共有 31 天。
print(calendar.monthrange(2023, 3))

print("%d年%d月%d日是星期%d" % (2023, 3, 10, calendar.weekday(2023, 3, 10) + 1))

# 返回一个字典, 包含(current scope)当前范围下的局部变量。
print(locals())

# 返回一个字典, 包含(current scope)当前范围下的全局变量。
print(globals())
