#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#


def maxDifference(px):
    stocks = len(px)
    maxDiff = px[1] - px[0]
    for i in range(2, stocks):
        for j in range(i-1, -1, -1):
            diff = px[i] - px[j]
            if(diff > maxDiff):
                maxDiff = diff
    if(maxDiff <= 0):
        return -1
    return maxDiff


"""
def maxDifference(px):
    stocks = len(px)
    maxDiff = max([px[i] - px[j] for i in range(1, stocks) for j in range(i-1, -1, -1)])
    if(maxDiff <= 0):
        return -1
    return maxDiff
"""
