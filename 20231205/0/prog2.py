import asyncio

async def snd(evsnd):
    evsnd.set()
    print('snd: generated evsnd')

async def mid1(evsnd, evmid1):
    await evsnd.wait()
    print('mid1: received evsnd')
    evmid1.set()
    print('mid1: generated evmid1')


async def mid2(evsnd, evmid2):
    await evsnd.wait()
    print('mid2: received evsnd')
    evmid2.set()
    print('mid2: generated evmid2')

async def rcv(evmid1, evmid2):
    await evmid1.wait()
    print('rcv: received evmid1')
    await evmid2.wait()
    print('rcv: received evmid2')


async def main():
    evsnd = asyncio.Event()
    evmid1 = asyncio.Event()
    evmid2 = asyncio.Event()
    await asyncio.gather(snd(evsnd), mid1(evsnd, evmid1), mid2(evsnd, evmid2), rcv(evmid1, evmid2))

asyncio.run(main())