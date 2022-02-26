from collections import deque
d = deque()

N = int(input())
for i in range(N):
    cmd = input().split()
    getattr(d, cmd[0])(*[cmd[1]] if len(cmd) > 1 else [])
print(*[item for item in d])


"""6
append 1
append 2
append 3
appendleft 4
pop
popleft"""