n = int(input()) # number of students subscribed to English newspaper
rollNumbersEnglish = map(int, input().split())
b = int(input()) # number of students subscribed to French newspaper
rollNumbersFrench = map(int, input().split())

# Output total number of students who have subscriptions to the English or the French newspaper but not both.
print(len(set(rollNumbersEnglish).symmetric_difference(rollNumbersFrench)))

"""
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Ans: 8
"""