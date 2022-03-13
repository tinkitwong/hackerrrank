"""
You are given two integer arrays of size NXP and MXP ( N & M  are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
Print the concatenated array of size (N+M)XP.


==Input
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Ans = 
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
"""

import numpy

N,M,P = list(map(int, input().split()))

arr_NP = []
arr_MP = []

# create NXP arr
for _ in range(N):
    row = list(map(int, input().split()))
    arr_NP.append(row)


# create MXP arr
for _ in range(M):
    row = list(map(int, input().split()))
    arr_MP.append(row)

# create numpy arr(s) NXP, MXP
arr_NP = numpy.array(arr_NP)
arr_MP = numpy.array(arr_MP)

# to keep P columns, concatenate along axis = 0 (rows)
print(numpy.concatenate((arr_NP, arr_MP),axis=0))