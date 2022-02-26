# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S,k = input().split()

S = "".join(sorted(S))
print(f"k {k}")

for permutation in list(permutations(S,int(k))):
    print("".join(permutation))
    

