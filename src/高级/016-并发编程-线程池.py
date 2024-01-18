from concurrent.futures import ThreadPoolExecutor

# 线程池
# 1. 线程池的大小
# 2. 线程池的任务
# 3. 线程池的关闭


def task(name: str):
    for i in range(1, 100):
        print(f"{name}-task-{i}\n", end="")


def main():
    with ThreadPoolExecutor(3) as pool:
        for i in range(1, 10):
            pool.submit(task, f"thread-{i}")


if __name__ == "__main__":
    main()
