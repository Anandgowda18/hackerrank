#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum_min = 0
    sum_max = 0
    for i in range(len(arr)-1):
        sum_min = sum_min + arr[i]
    for j in range(1,len(arr)):
        sum_max = sum_max+arr[j]
    print(sum_min,sum_max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
