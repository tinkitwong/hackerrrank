from itertools import groupby

S = "1222311"

print(*[(len(list(g)),int(k)) for k, g in groupby(S)])

