_ = input().split()
arr, set_A, set_B = input().split(), set(input().split()), set(input().split())
happiness = 0

print(sum([(i in set_A) - (i in set_B) for i in arr]))