# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

def namedTuple():
    N = int(input())
    marks = []
    student = namedtuple('Student', input())

    for i in range(N):
        marks.append(int(student(*input().split()).MARKS))
        
    avg = sum(marks) / N
    print(f"{avg:.2f}")

"""
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   """

"""
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5"""