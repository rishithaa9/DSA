def insertionsort(arr):
    n=len(arr)
    j=0
    for i in range(n):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            
    return arr
    
print(insertionsort(arr=[9,3,8,5,2,1]))