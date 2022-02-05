#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairCount = 0 
    seen = {}
    # iterate through the list
    # if not seen in {}, add it to {}
    for sock in ar:
        if sock not in seen:
            seen[sock] = 1
        else:
            seen[sock] += 1
    
    for k, v in seen.items():
        if v % 2 == 0: 
            pairCount += v / 2
        if v % 2 != 0 and v > 2:
            pairCount += int( v / 2 )
    print(seen)
    return pairCount

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
