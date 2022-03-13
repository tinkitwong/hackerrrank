"""
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, 
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.


==Input
3 3 3

Ans = 

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
"""
import numpy as np

vals = tuple(map(int, input().split()))

print(np.zeros(vals, dtype=np.int32))
print(np.ones(vals, dtype=np.int32))