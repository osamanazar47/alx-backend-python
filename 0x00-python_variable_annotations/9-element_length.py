#!/usr/bin/env python3
'''
Task 9 module.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(n, len(n)) for n in lst]
