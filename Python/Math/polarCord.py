# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
from math import sqrt
z = complex(input())


phi = phase(z)
radius = sqrt(z.real**2 + z.imag**2)
# print r
print(radius)
# print phi
print(phi)  
