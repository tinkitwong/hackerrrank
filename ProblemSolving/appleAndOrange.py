#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def checkConstraints(var) -> bool:
    if var not in range(1,10**5+1): return False
    return True
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # constraints
    variables = [s,t,a,b,len(apples),len(oranges)]
    for var in variables: 
        if checkConstraints(var) == False: 
            return False
    if not a < s < t < b : return False
    
    appleCount = 0
    orangeCount = 0
    
    for i in range(len(apples)):
        if ( apples[i] + a ) in range(s,t+1): appleCount += 1 
    for j in range(len(oranges)):
        if ( oranges[j] + b ) in range(s,t+1): orangeCount += 1 
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
