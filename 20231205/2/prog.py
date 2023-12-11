import asyncio
import random


async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()
    idx = start
    first_half_idx = start
    second_half_idx = middle

    while first_half_idx < middle and second_half_idx < finish:
        if A[first_half_idx] < A[second_half_idx]:
            B[idx] = A[first_half_idx]
            first_half_idx += 1
        else:
            B[idx] = A[second_half_idx]
            second_half_idx += 1
        idx += 1
    
    while first_half_idx < middle:
        B[idx] = A[first_half_idx]
        idx += 1
        first_half_idx += 1

    while second_half_idx < finish:
        B[idx] = A[second_half_idx]
        idx += 1
        second_half_idx += 1
    
    event_out.set()
    

async def mtasks(A):
    A = A[:]
    N = len(A)
    B = [None] * N
    events = []
    for _ in range(N + 1):
        event = asyncio.Event()
        event.set()
        events.append(event)
    
    tasks, step, parity = [], 1, True
    while step < N:
        new_events = []
        event_idx = 0
        idx = 0
        for idx in range(0, N, step * 2):
            start = idx
            finish = min(idx + step * 2, N)
            middle = min(start + step, N)
            new_event = asyncio.Event()
            events[event_idx].set()
            task = asyncio.create_task(
                merge(
                    A, B,
                    start,
                    middle,
                    finish,
                    events[event_idx],
                    events[event_idx + 1],
                    new_event
                    )
                )
            tasks.append(task)
            new_events.append(new_event)
            event_idx += 2
        A, B = B, A
        parity = not parity
        events += new_events + [new_event]
        step *= 2

        if parity:
            result = tasks, A
        else: 
            result = tasks, B

    return result 

import sys
exec(sys.stdin.read())
