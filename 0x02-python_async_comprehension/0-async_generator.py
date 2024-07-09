#!/usr/bin/env python3
""" Module for the first task in in python async comprehension"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """a corountine that loops 10 times"""
    for number in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
