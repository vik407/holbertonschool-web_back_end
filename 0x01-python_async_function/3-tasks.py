#!/usr/bin/env python3
""" 3. Tasks
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Take the integer on max delay and return the task
    """
    return asyncio.create_task(wait_random(max_delay))
