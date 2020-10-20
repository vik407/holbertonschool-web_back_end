#!/usr/bin/env python3
""" 7. Complex types - string and int/float to tuple
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple.
    """
    return (k, v**2)
