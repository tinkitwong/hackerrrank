"""You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

== Input
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Ans = 
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""
import numpy as np

arr_A = np.array(list(map(np.float32, input().split())), dtype=np.float32)
print(np.floor(arr_A))
print(np.ceil(arr_A))
print(np.rint(arr_A))
