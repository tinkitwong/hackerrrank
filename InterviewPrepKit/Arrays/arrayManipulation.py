def arrayManipulation(n, queries):
    # use prefix sum method
    
    # initialize array
    arr = [0] * (n+2)
    
    # perform query operations
    for a,b,k in queries:
        arr[a] += k
        arr[b+1] -= k
    
    # find the max
    maximum = temp = 0
    for val in arr:
        temp += val
        maximum = max(maximum, temp)
    return maximum

n=5
queries = [[1,2,100],[2,5,100],[3,4,100]]
print(arrayManipulation(n,queries))
    