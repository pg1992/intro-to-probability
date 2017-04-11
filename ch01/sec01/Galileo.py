#!/usr/bin/env python

"""
This module contains the solution of the problem 3
from section 1.1 of the book 'Introduction to Probability'
by Grinstead and Snell.
"""

import sys
import numpy as np

def sumsProportions(num_throws:int=1000, dice_qty:int=3, sums_list:list=[9,10]) -> list:
    """Simulates a random experiment of 'num_throws' of 'dice_qty' dice.

    After the random experiment the sum of the dice is compared
    with the values in 'sums_list' and the proportion of events
    that resulted in the respective sum is returned in a list.
    """

    outcomes = np.floor(6 * np.random.random((num_throws, dice_qty))) + 1
    out_sums = outcomes.sum(axis=1)

    result = list()

    for sums in sums_list:
        result.append((out_sums == sums).sum() / float(num_throws))
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sumsProportions(num_throws = int(sys.argv[1])))
    else:
        print(sumsProportions())
