"""
tourists:
-> captain
-> An unknown group of families consisting of K members per group where K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

==Input==
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Ans = 8
"""

# from collections import Counter
# K = int(input()) # size of each group
# roomNumbers = map(int, input().split())# unordered elements of the room number list

# counter = Counter(roomNumbers)
# # find the roomNumber that occured only once; output the captain number
# print(counter.most_common()[-1][0])


k, rooms, single, multiple = input(), input().split(), set(), set()

for room in rooms: single.add(room) if room not in single else multiple.add(room)

print(single.difference(multiple).pop())