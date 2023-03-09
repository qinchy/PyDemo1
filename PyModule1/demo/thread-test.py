#!/usr/bin/python3

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadid, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = name
        self.delay = delay

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadname, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadname, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()

if __name__ == '__main__':
    threads = []

    # 创建新线程
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
