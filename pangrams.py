#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    # Write your code here
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for x in s:
        if x.upper() in alpha:
            alpha.remove(x.upper())
    # print(alpha)
    if len(alpha) == 0:
        return "pangram"
    else:
        return "not pangram"


if __name__ == "__main__":

    s = input()

    result = pangrams(s)

    print(result)
