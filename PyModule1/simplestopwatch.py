import time

print('按任意键开始计时，按下 Ctrl + C 停止计时。')
while True:
    # 如果是 python 2.x 版本请使用 raw_input()
    input("")  
    starttime = time.time()
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')
        break