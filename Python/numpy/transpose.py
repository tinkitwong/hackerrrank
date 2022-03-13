"""
You are given a MXM integer array matrix with space separated elements ( N = rows and  M = columns).
Your task is to print the transpose and flatten results.

== Input
2 2
1 2
3 4

Ans =
[[1 3]
 [2 4]]
[1 2 3 4]
"""
import numpy

N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
arr = numpy.array(arr)
numpy.reshape(arr, (N, M))
print(numpy.transpose(arr))
print(arr.flatten())