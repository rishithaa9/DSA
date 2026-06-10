def recursion(arr):
    if (len(arr))==0:
       return 0
    smalloutput=recursion(arr[1:])
    return arr[0]+smalloutput
l=[1,2,3,4,5]
print(recursion(l))