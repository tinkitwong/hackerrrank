"""
Given two integer arrays, A and B of dimensions NXM
Your task: 
1. Add
2. Subtract
3. Multiply
4. Integer Division
5. Mod
6. Power

Note: There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

== Input
1 4
1 2 3 4
5 6 7 8

Ans = 
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] """

import numpy as np

N,M = tuple(map(int, input().split()))
arr_A = []
arr_B = []
for i in range(N):
    arr_A.append(list(map(int, input().split())))

for i in range(N):
    arr_B.append(list(map(int, input().split())))

arr_A, arr_B = np.array(arr_A, dtype=np.int32), np.array(arr_B, dtype=np.int32)

# perform operations
print(np.add(arr_A, arr_B))
print(np.subtract(arr_A, arr_B))
print(np.multiply(arr_A, arr_B))
print(np.floor_divide(arr_A, arr_B)) 
print(np.remainder(arr_A, arr_B))
print(np.power(arr_A, arr_B))

