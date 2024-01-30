import asyncio

# 执行流程
# 1. 事件循环里首先添加了 main 任务
# 2. 开始执行 main 任务
# 3. main 中遇到了 await 执行另一个任务
# 4. main 开始等待另一个任务结束
# 5. 另一个任务结束后，main 继续执行下面的代码


# 1. 定义协程
async def calc(n1: int, n2: int) -> int:
    print(f"calc {n1} + {n2}")
    return n1 + n2


async def main():
    print("main step1")
    # 3. 协程里添加另一个协程，也就是往事件循环添加另一个任务
    r1 = await calc(1, 2)
    print("main step2")
    print(f"r1:{r1}")


if __name__ == "__main__":
    # 2. 事件循环添加任务
    asyncio.run(main())
