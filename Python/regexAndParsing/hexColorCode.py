# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

inBlock = False
pattern = '(?<!^)(#(?:[\da-fA-F]{3}){1,2})'
for i in range(int(input())):
    
    line = input()  
    
    if '{' in line:
        inBlock = True
        continue
    elif '}' in line:
        inBlock = False
        continue
    else:
        if inBlock:
            result = re.findall(pattern, line)
            if result:
                print(*result, sep='\n')
            