"""
check if set_A is a subset of set_B

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Ans = True, False, False
"""

T = int(input()) # T number of test cases
for _ in range(T):
    # get inputs
    numElements_setA = int(input()) 
    set_A = set(map(int, input().split()))
    numElements_setB = int(input()) 
    set_B = set(map(int, input().split()))

    # check if set_A is a subset of set_B
    print(set_A.issubset(set_B))

