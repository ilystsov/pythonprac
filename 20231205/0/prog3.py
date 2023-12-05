import itertools
import asyncio
async def prod(q1):
    for i in range(5):
        await q1.put(f'value_{i}')
        print(f'prod: put {i} to q1')
        await asyncio.sleep(1)

async def mid(q1):
    for i in itertools.count(start=1):
        item = await q1.get()
        print(f'mid: got {item} from q1')
        await q2.put(item)
        print(f'mid: put {i} to q2')



async def cons(q2):
    for i in itertools.count(start=1):
        item = await q2.get()
        print(f'cons: got {item} from q2')


async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    await asyncio.gather(prod(q1), cons(q2), mid(q1))
