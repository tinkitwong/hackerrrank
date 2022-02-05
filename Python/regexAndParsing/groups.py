import re
S = 12345678910111213141516171820212223
m = re.search(r'([a-zA-Z0-9])\1', str(S))

print(m.group(1) if m else -1)