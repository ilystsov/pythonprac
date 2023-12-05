import asyncio
async def squarer(a):
    return a * a

async def doubler(a):
    return a + a

def main():
    x, y = eval(input())
    res = await asyncio.gather(squarer(x), squarer(y))
    res = await asyncio.gather(doubler(res[0]), doubler(res[1]))

asyncio.run(main())