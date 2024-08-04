#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def rev_col(matrix, col):
    n2 = len(matrix)
    i, j = 0, col
    while i < int(n2 / 2):
        matrix[i][j], matrix[n2 - 1 - i][j] = matrix[n2 - 1 - i][j], matrix[i][j]
        i += 1
    return matrix


def rev_row(matrix, row):
    matrix[row] = list(reversed(matrix[row]))
    return matrix


# def flippingMatrix(matrix):
#     # Write your code here
#     print("Original mtr")
#     for row in matrix:
#         print(row)

#     n2 = len(matrix)
#     n1 = int(n2 / 2)
#     j = 0
#     while j < n2:
#         i = 0
#         s1, s2 = 0, 0
#         while i < n1:
#             s1 += matrix[i][j]
#             s2 += matrix[n2 - 1 - i][j]
#             i += 1
#         if s1 < s2:
#             matrix = rev_col(matrix, col=j)
#         j += 1

#     print("Col rev mtr")
#     for row in matrix:
#         print(row)

#     for i in range(n1):
#         if sum(matrix[i][:n1]) < sum(matrix[i][n1:]):
#             matrix = rev_row(matrix, row=i)


#     print("Row rev final mtr")
#     return matrix
def flippingMatrix(matrix: list[list[int]]) -> int:
    """
    Since any number of column/row flips are possible,
    The maximum values must come from rotations around the center.
    Also, since the problem doesn't require the resultant matrix,
    we can simply determine the largest values for each position
    then return their sum.
    q=4
    n=q/2
    m=[
      [ 1, 2, 3, 4],
      [ 5, 6, 7, 8],
      [ 9,10,11,12],
      [13,14,15,16],
    ]
    # Top left quad must consist of max for each rotation:
    # 0,0:max([1,4,13,16]) 0,1:max([2,3,14,15])
    # 1,0:max([5,8,9,12])  1,1:max([6,7,10,11])

    Generalized, these can be represented as follows:
    r,c: max([m[r][c], m[r][q-1-c], m[q-1-r][c], m[q-1-r][q-1-c]])

    find the max value for each r,c set
    return the sum of max values
    """

    n2 = len(matrix)
    n1 = n2 // 2
    m = matrix
    tsum = 0

    for r in range(n1):
        for c in range(n1):
            tsum += max(
                [m[r][c], m[r][n2 - 1 - c], m[n2 - 1 - r][c], m[n2 - 1 - r][n2 - 1 - c]]
            )

    return tsum


if __name__ == "__main__":

    # q = int(input().strip())
    q = 1

    for q_itr in range(q):
        # n = int(input().strip())
        n = 2

        matrix = []

        # for _ in range(2 * n):
        #     matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(
            [
                [112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 43],
                [62, 98, 114, 108],
            ]
        )

        print(result)
