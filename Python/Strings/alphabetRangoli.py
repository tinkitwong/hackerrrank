import string

def print_rangoli(size):
    # your code goes here
    
    alpha = string.ascii_lowercase
    # for i in range(size):  # rows 
    L = []
    n = size
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print(L)
    print('\n'.join(L[:0:-1]+L))
            
        
    
if __name__ == '__main__':
    n = 5
    print_rangoli(n)