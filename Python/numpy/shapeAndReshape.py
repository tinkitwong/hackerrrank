"""
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.


== Input
1 2 3 4 5 6 7 8 9

Ans = 
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
import numpy
arr = list(map(int, input().split()))

# convert into 3X3 Numpy Arr
print(numpy.reshape(arr, (3,3)))
