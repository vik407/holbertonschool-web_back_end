#!/usr/bin/env python3
""" 8. Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float.
    """
    return lambda x: x * multiplier
