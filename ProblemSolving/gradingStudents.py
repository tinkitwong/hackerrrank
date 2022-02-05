#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    n = len(grades)
    ERRCODE = -1
    # constraints
    if n not in range(1,61): return ERRCODE
    
    # 1, 2, 3, 4, 5
    
    for i in range(n):
        if grades[i] not in range(0,101): return ERRCODE 
        nextMultiple = - ( - grades[i] // 5 )  * 5 # calculate the next Multiple without libraries
        if nextMultiple - grades[i] < 3 and grades[i] >= 38: grades[i] = nextMultiple # reassign the value to the next multiple of 5      
        
    # return grades after rounding
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
