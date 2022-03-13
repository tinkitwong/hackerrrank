"""Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.

== Input
3 3

Ans =
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""

import numpy as np
np.set_printoptions(legacy='1.13')
vals = tuple(map(int, input().split()))

print(np.eye(*vals))

