#!/usr/bin/env python3
""" module for task 2"""
import asyncio
import time
from typing import Callable


# Assuming wait_n is imported from your previous file where it's defined
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure average execution time for wait_n(n, max_delay)"""
    start_time = time.time()

    # Run wait_n asynchronously
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    # Calculate average time per operation
    average_time = total_time / n

    return average_time
