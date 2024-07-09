#!/usr/bin/env python3
""" Module for the first task Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a corountine that loops 10 times"""
    for number in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
