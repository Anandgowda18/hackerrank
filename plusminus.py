#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count = len(arr)
    flag_pos = 0
    flag_neg = 0
    flag_zero = 0
    for i in range(count):
        if arr[i] > 0:
            flag_pos = flag_pos + 1
        elif arr[i] < 0:
            flag_neg = flag_neg + 1
        else:
            flag_zero = flag_zero + 1
    print(flag_pos/count)
    print(flag_neg/count)
    print(flag_zero/count)       
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
