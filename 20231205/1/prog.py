import itertools
import asyncio


event = asyncio.Event()


async def writer(queue, delay):
    for number in itertools.count(start=0):
        await asyncio.sleep(delay)
        await queue.put(f'{number}_{delay}')
        if event.is_set():
            return

async def stacker(queue, stack):
    while not event.is_set():
        item = await queue.get()
        await stack.put(item)

async def reader(stack, amount, delay):
    for _ in range(amount):
        await asyncio.sleep(delay)
        item = await stack.get()
        print(item)
    event.set()

async def main():
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    delay1, delay2, delay3, amount = eval(input())
    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        reader(stack, amount, delay3),
        stacker(queue, stack),
    )

asyncio.run(main())
