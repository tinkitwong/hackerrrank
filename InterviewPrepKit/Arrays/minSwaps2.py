# def minimumSwaps(arr):
#     swaps = 0
#     for i in range(1,len(arr)+1):
#         if i-1 != arr.index(i):
#             # print(arr)
#             # print("if {} != {}".format(i-1, arr.index(i)))
#             # print("swapping {} and {}".format(arr[arr.index(i)], arr[i-1]))
#             arr[arr.index(i)], arr[i-1] = arr[i-1], arr[arr.index(i)]
#             swaps +=1 
#     return swaps

def minimumSwaps(arr):
    a = dict(enumerate(arr,1))
    b = {v:k for k,v in a.items()}
    count = 0
    for i in a:
        x = a[i] 
        if x != i: # if index != value
            y = b[i]  # y = value's index           
            a[y] = x # swap current index value with the value at the index. 
            a[i] = i # swap in place
            b[x] = y # update dictionary b's val:index 
            count += 1
    print(a)
    return count


arr = [1,3,5,2,4,6,7]
print(minimumSwaps(arr))
