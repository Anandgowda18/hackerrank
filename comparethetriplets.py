#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    flag_alice=0
    flag_bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            flag_alice = flag_alice + 1
        elif a[i]<b[i]:
            flag_bob = flag_bob + 1
        else:
            pass
    return [flag_alice,flag_bob]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
