# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

n = int(input())
for _ in range(n):
    name, emailAddr = email.utils.parseaddr(input())
    
    # perform regex on email address
    result = re.fullmatch('^[a-zA-Z0-9][a-zA-Z0-9-._]+@[a-zA-Z]+\.+[a-z]{1,3}$', emailAddr)
    
    if result:
        print(email.utils.formataddr((name, emailAddr)))
    
    
    
        
