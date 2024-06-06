#!/usr/bin/env python3

""" mixed list module"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  This returns sum as a float. """
    return float(sum(mxd_lst))
