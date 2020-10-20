#!/usr/bin/env python3
""" 6. Complex types - mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns list of floats/int
    """
    return sum(mxd_list)
