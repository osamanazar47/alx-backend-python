#!/usr/bin/env python3
"""module for task 4 (task_wait_random)"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns sorted wait times."""
    w_t = await asyncio.gather(*(task_wait_random(max_delay)for i in range(n)))
    return sorted(w_t)
