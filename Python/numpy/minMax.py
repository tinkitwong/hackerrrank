import numpy
from sys import stdin

my_array = []

for line in stdin:
    my_array.append(list(map(int, line.split())))
    
my_array = numpy.array(my_array)
print(max(numpy.min(my_array, axis=1)))
    
    

