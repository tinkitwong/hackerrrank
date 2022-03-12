"""
Given set A and n other sets
Your job is to find whether set A is a strict superset of each of the N sets.
Print True if  A is a strict superset of each of the N sets; Otherwise, print False
A strict superset has at least one element that does not exist in its subset.


1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Ans = False
"""

set_A = set(map(int, input().split()))
n = int(input()) # number of elements of other sets
output = True

for _ in range(n):
    set_other = set(map(int, input().split()))
    # check if set_A is a strict superset of set_other
    if not set_A.issuperset(set_other) or len(set_A) - len(set_other) == 0:
        output = False
        break
        
print(output)
        


# print(sum([(i in set_A) - (i in set_B) for i in arr]))