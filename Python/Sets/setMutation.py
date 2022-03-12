"""
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .


16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

Ans = 38
"""

n = int(input()) # number of elements in set A
set_A = set(map(int, input().split()))
N = int(input()) # N is the number of other sets
# next 2 * N lines
for _ in range(N):
    # first line -> "operation_name length_of_other_set"
    op, len_other = input().split()
    # second line -> "other set"
    other_set = set(map(int, input().split()))
    # perform operation on set_A
    getattr(set_A, op)(other_set)

# Output the sum of elements in set A.
print(sum(set_A))

