# 线程锁
# 多个线程访问同一块数据可能产生数据丢失，覆盖，不完整等问题
# 这叫线程同步问题
# 锁可以解决线程同步问题


import threading

# 全局变量
count = 0
lock = threading.Lock()


def increment():
    global count
    for _ in range(1000000):
        # 多个线程修改共用资源要加锁
        # count是共用资源
        # 不加锁，结果可能是错误的
        # 不加锁的话，由于Python中的全局解释器锁（Global Interpreter Lock）的存在，多个线程无法同时执行Python字节码，因此代码中的每个线程实际上是交替执行的。这意味着每个线程在增加count变量之前都要获取GIL，然后释放GIL，这样可能会导致一些增加操作被覆盖，从而导致最终的结果小于预期值。
        lock.acquire()
        count += 1
        lock.release()


threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(count)
