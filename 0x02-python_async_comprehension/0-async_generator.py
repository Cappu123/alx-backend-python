#!/usr/bin/env python3
"""module """

import asyncio
import random

async def async_generator():
    """generates 10 random numbers sequence """

    for i in range(10):
        await asyncio.sleep(1)
        num = random.random() * 10
        yield num
