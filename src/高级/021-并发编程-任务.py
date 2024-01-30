import asyncio
import time


async def call_api(name: str, delay: float):
    print(f"name-{name},delay={delay},step1")
    # 模拟等待
    await asyncio.sleep(delay)
    print(f"name-{name},step2")


async def main():
    t = time.perf_counter()
    print("start a task")
    await call_api("a", 3)
    print("finished a task")
    print("start b task")
    await call_api("b", 2)
    print("finished b task")
    print(f"time={time.perf_counter() - t}")


async def main1():
    t = time.perf_counter()
    tasks = []
    # 把任务提前丢到事件循环中
    t1 = asyncio.create_task(call_api("a", 3))
    t2 = asyncio.create_task(call_api("b", 2))
    tasks.append(t1)
    tasks.append(t2)
    for task in tasks:
        await task
    print(f"time={time.perf_counter() - t}")


if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(main1())
