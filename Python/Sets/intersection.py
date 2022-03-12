"""
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Ans: 5
"""

n = int(input()) # number of students subscribed to English newspaper
rollNumbersEnglish = map(int, input().split())
b = int(input()) # number of students subscribed to French newspaper
rollNumbersFrench = map(int, input().split())

# output total number of students who have both subscriptions
print(len(set(rollNumbersEnglish).intersection(rollNumbersFrench)))