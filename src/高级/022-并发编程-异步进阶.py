import asyncio


async def play_music(music: str, delay: float):
    print(f"start play {music}")
    await asyncio.sleep(delay)
    print(f"finished play {music}")


async def my_cancel():
    task = asyncio.create_task(play_music("青花瓷", 2))
    await asyncio.sleep(2)

    if not task.done():
        task.cancel()
        print("cancel task")


async def my_cancel_timeout():
    task = asyncio.create_task(play_music("青花瓷", 5))
    try:
        await asyncio.wait_for(task, 3)
    except asyncio.TimeoutError:
        # task.cancel()
        print("超时")


async def my_timeout():
    task = asyncio.create_task(play_music("青花瓷", 5))
    try:
        await asyncio.wait_for(asyncio.shield(task), 3)
    except asyncio.TimeoutError:
        # task.cancel()
        print("超时")
        await task


# 语法糖，往事件循环同时添加多个任务并等待执行完毕
async def my_gather():
    results = await asyncio.gather(play_music("青花瓷01", 2), play_music("青花瓷02", 3))
    print(f"{results}")


async def call_api():
    print("call api...")
    raise Exception("error call api")


async def my_gather_with_execption():
    results = await asyncio.gather(
        play_music("青花瓷01", 2),
        call_api(),
        return_exceptions=True,
    )
    print(f"{results}")


async def main():
    # 取消
    # await my_cancel()
    # 超时取消
    # await my_cancel_timeout()
    # 超时不取消
    # await my_timeout()
    # 语法躺多个任务执行
    # await my_gather()
    # 避免异常程序崩溃
    await my_gather_with_execption()


if __name__ == "__main__":
    asyncio.run(main())
