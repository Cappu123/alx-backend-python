#!/usr/bin/env python3
'''Task 6 module
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''takes in mxd_lst of int and float, returns sum as float
    '''
    return float(sum(mxd_lst))
