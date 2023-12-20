import datetime
import time

if __name__ == '__main__':
    a1 = "2019-5-10 23:40:00"
    # 先转换为时间数组
    timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

    # 转换为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)

    # 格式转换 - 转为 /
    a2 = "2019/5/10 23:40:00"
    # 先转换为时间数组,然后转换为其他格式
    timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    print(otherStyleTime)

    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
    # 转换为时间戳
    timeStamp = int(time.mktime(threeDayAgo.timetuple()))
    # 转换为其他字符串格式
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)

    # 给定时间戳
    timeStamp = 1557502800
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    threeDayAgo = dateArray - datetime.timedelta(days=3)
    print(threeDayAgo)

    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
