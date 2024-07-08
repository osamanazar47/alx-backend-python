#!/usr/bin/env python3
"""module for the first task about the basic async usage.
"""
import asyncio
import random


async def wait_random(max_delay=10):
  """A coroutines that awaits for a random delay and returns it"""
  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay
