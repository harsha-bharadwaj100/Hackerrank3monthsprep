#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def twoArrays(k, A, B):
    # Write your code here
    newA = sorted(A)[::-1]
    newB = sorted(B)
    sumAB = [(a + b) for a, b in zip(newA, newB)]
    for i in sumAB:
        if i < k:
            return "NO"
    return "YES"


print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
# if __name__ == "__main__":

#     q = int(input().strip())

#     for q_itr in range(q):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         k = int(first_multiple_input[1])

#         A = list(map(int, input().rstrip().split()))

#         B = list(map(int, input().rstrip().split()))

#         result = twoArrays(k, A, B)

#         print(result)
