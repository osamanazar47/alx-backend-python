#!/usr/bin/env python3
''' the module for task 12. '''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Creates multiple copies of items in a tuple.
    '''
    zoomed_inside: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_inside


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
