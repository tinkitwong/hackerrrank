def a(values, commands):
    n = 9
    s = set(map(int, values))
    N = 10
    for _ in range(N):
        command = commands[_].split()
        print(command, s)
        getattr(s, command[0])(*[int(command[1])] if len(command) > 1 else [])
    print(sum(s))
    # print(cmd)
    # print(*[item for item in cmd])

values = [1,2,3,4,5,6,7,8,9]
commands = ["pop", "remove 9", "discard 9", "discard 8", "remove 7", "pop", "discard 6", "remove 5", "pop", "discard 5"]
a(values, commands)


"""
from collections import deque
d = deque()

N = int(input())
for i in range(N):
    cmd = input().split()
    getattr(d, cmd[0])(*[cmd[1]] if len(cmd) > 1 else [])
print(*[item for item in d])
"""

