# 线程安全队列
# queue模块中的Queue类提供了线程安全队列功能
# 下面是一个生产者消费者例子

import queue
import threading
import time

q = queue.Queue(maxsize=10)


def task():
    while True:
        # 从队列获取数据
        time.sleep(0)
        item = q.get()
        print(f"task get {item} size:{q.qsize()}")


def main():
    print(q)
    t1 = threading.Thread(target=task)
    # 守护线程
    t1.daemon = True
    t1.start()

    print("main continue")
    for i in range(1000):
        # 往队列塞数据
        # time.sleep(0.01)
        q.put(f"i-{i}")


if __name__ == "__main__":
    main()
