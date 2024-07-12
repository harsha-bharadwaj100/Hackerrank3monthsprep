#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps: int, path: str):
    # Write your code here
    intpath = []
    vcount = 0
    refsum = 0
    refsumpath = [0]
    for i in path:
        if i == "U":
            intpath.append(1)
        elif i == "D":
            intpath.append(-1)
    for x in intpath:
        refsum += x
        refsumpath.append(refsum)
    for i in range(len(refsumpath) - 1):
        if refsumpath[i] == 0 and refsumpath[i + 1] < 0:
            vcount += 1
    return vcount


if __name__ == "__main__":

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
