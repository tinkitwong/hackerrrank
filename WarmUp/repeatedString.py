#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    ERRCODE = -1 
    # constraints
    # if abs(s) not in range(1,101): return ERRCODE
    if n not in range(1,10**12 + 1): return ERRCODE

    # create final string
    """
    noOfRepeats = math.trunc(n / len(s))
    noOfCarryOverCharacters =  n % len(s)
    answer = ( noOfRepeats * s ).count("a") + s[:noOfCarryOverCharacters].count("a")
    """
    # count number of a in s
    # count number of repeated s
    # count number of a in trailing s
    answer = ( ( n // len(s) ) * s.count("a") ) + s[:n % len(s)].count("a")

    # count number of occurances of "s" in final string
    print(answer)
    

    # print freq of a in the substring

if __name__ == '__main__':
    s = "a"
    n = 1000000000000
    print(repeatedString(s,n))