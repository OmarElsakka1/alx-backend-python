#!/usr/bin/env python3
""" The first element of a sequence """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This is the Safe first element """
    if lst:
        return lst[0]
    else:
        return None
