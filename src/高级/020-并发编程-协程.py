import asyncio
import time


async def call_api():
    print("Hello")
    await asyncio.sleep(3)
    print("World")


async def main():
    start = time.perf_counter()
    hello1 = asyncio.create_task(call_api())
    hello2 = asyncio.create_task(call_api())
    tasks = [hello1, hello2]
    while True:
        tasks = [t for t in tasks if not t.done()]
        if len(tasks) == 0:
            end = time.perf_counter()
            print(f"It took {end - start} second(s) to complete.")
            break
        await tasks[0]


asyncio.run(main())
