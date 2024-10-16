#!/usr/bin/env python3

""" This module is about a random async operation
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    wait asynchronously for a random delay
    :param max_delay:
    :return:
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
