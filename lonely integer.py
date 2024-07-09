#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a, n):
    # Write your code here
    count = dict()
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count, a


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a, n)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
