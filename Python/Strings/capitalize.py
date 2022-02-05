#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    """
    this method keeps track of in between spaces
    """
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    s = "hello    world lol"
    result = solve(s)
    print(result)