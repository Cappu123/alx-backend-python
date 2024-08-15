#!/usr/bin/env python3

'''module of Task7
'''
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its valu
    '''

    sqr = float(v ** 2)
    return [k, sqr]
