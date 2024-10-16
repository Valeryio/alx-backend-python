#!/usr/bin/env python3

""" This module is about a random async operation
"""

import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.random(0, max_delay)
    asyncio.sleep(delay)
    return delay