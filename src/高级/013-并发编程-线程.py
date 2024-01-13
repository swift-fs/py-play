# 进程，资源分配的最小单元
# 进程，操作系统支持多进程同时执行，叫并发
# 线程，CPU调度的最小单元
# 线程，共享进程的内存，CPU等资源
# 一个进程中可以同时运行多个线程，叫并发


import threading
import time


def task(name):
    for i in range(1, 100):
        print(f"{name}:{i}")


# 线程类
class TaskThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        for i in range(1, 100):
            print(f"{self.name}:{i}\n", end="")
            time.sleep(0.01)


def main():
    # 串行执行
    # task("taks-01")
    # task("taks-02")

    # 并发执行
    t1 = threading.Thread(target=task, args=("taks-01",))
    t2 = threading.Thread(target=task, args=("taks-02",))
    t1.start()
    print("t1 start")
    t2.start()
    print("t2 start")
    # 等待t1结束
    # t1.join()
    # 等待t2结束
    # t2.join()

    # 通过继承线程类，并发执行
    t3 = TaskThread("taks-03")
    t4 = TaskThread("taks-04")
    # 守护线程，主线程结束，子线程自动结束
    # 主线程必须等非守护线程全部结束才会退出执行
    # 守护线程一般用于非关键性的线程，譬如日志
    # t3.setDaemon(True)
    # t4.setDaemon(True)
    t3.start()
    t4.start()
    # t3.join()
    # t4.join()

    print("main end")


if __name__ == "__main__":
    main()
