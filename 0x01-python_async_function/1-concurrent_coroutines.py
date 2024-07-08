#!/usr/bin/env python3
"""A module for task 1
task for executing multiple coroutines
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ returns a list of radom ascending delay values"""
    delay_list: list[float] = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delay_list)
