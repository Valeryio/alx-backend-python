#!/usr/bin/env python3

"""
This module contains the measure_time function
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int):
    """
    This function measure the time used by an async function
    :param n:
    :param max_delay:
    :return:
    """
    start_time = time.time()

    result = await wait_n(n, max_delay)

    elapsed_time = time.time() - start_time
    return elapsed_time
