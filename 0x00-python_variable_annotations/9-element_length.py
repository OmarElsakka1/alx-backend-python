#!/usr/bin/env python3
""" module of typing an iterable object"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return Element length """
    return [(i, len(i)) for i in lst]
