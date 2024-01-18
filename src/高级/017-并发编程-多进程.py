from concurrent.futures import ProcessPoolExecutor
import os
import multiprocessing

# 多进程


def task(name: str, num: int):
    for i in range(1, num):
        print(f"{name}-pid-{os.getpid()}-{i}\n", end="")


def main():
    core_count = multiprocessing.cpu_count()
    print(f"core_count:{core_count}")
    with ProcessPoolExecutor(core_count) as pool:
        for i in range(1, 10):
            pool.submit(task, f"task-{i}", 100)


if __name__ == "__main__":
    main()
