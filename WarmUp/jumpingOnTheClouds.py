#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    minJumpCount = 1000000000000000000000
    n = len(c)
    seen = {}
    ALLOWEDVALS = [0,1]
    ERRCODE = -1 
    
    """Cases
    1. can jump once
    2. can jump twice
    """ 
    # constraints / cases 
    if n not in range(2, 101): return ERRCODE
    if c[0] != c[n-1] and c[0] != 0: return ERRCODE
    for i in range(len(c)):
        if c[i] not in ALLOWEDVALS: return ERRCODE
        
        # add c to seen dictionary for O(1) lookup time
        if i not in seen:
            seen[i] = c[i]
    """
    - dict containing indexes of non-safe cloud indices
    - get the indices of non-safe clouds 
    - check how many jumps we can make eg. [0,1,0,0,0,1,0]
    
    What we have
    - size of c : len(c)
    - indices of non-safe cloud in dict
    
    Steps
    - initiate minJumpCount
    - looking at the first index of non-safe cloud -> eg. index = 1 , check if index+2 is safe.
    - if not safe, then check if index+1 is safe.
    - if any of the above cases are safe, then update minJumpCount accordinly
    - return minJumpCount 
    """
    currentPosition = 0
    jumpCount = 0
    print(c)
    while currentPosition <= n-1:
        print(f"currentPosition {currentPosition}")
        if (currentPosition+2) <= n-1 and c[currentPosition+2] == 0:
            currentPosition += 2         
            jumpCount += 1
        elif (currentPosition+1) <= n-1 and c[currentPosition+1] == 0:
            currentPosition += 1
            jumpCount += 1
        elif currentPosition == n-1:
            break
        else:
            print(c)
            print(f"currentPosition {currentPosition} | jumpCount {jumpCount} | n {n} | c[jumpCount+1] {c[jumpCount+1]}")
            return ERRCODE
    # return min jumps needed to win the game
    return jumpCount 

if __name__ == '__main__':
    c = [0,0,0,1,0,0]
    print(jumpingOnClouds(c))
