#!/usr/bin/env python3
"""module """

import asyncio
import random

async def async_generator():
    """async generator function """

    for i in range (10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
