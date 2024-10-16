#!/usr/bin/env python3

"""THis module run concurrents coroutines
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay:int):
    """
    wait asynchronously multiple time for a random delay
    :param n:
    :param max_delay:
    :return: list of tasks
    """
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i in range(n):
            task = tg.create_task(wait_random(max_delay))
            tasks.append(task)

    result = [task.result() for task in tasks]
    result.sort()

    return result
