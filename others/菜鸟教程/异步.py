import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    await hello()

# loop是个死循环 | 遇到阻塞就下一个任务
loop=asyncio.get_event_loop()
loop.run_until_complete(main())

asyncio.run(main())