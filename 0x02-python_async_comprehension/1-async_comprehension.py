#!/usr/bin/env python3
"""Module for the second task Async Comprehension"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The corountine that will return the 10 random nums"""
    return [num async for num in async_generator()]
