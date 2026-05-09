def bubblesort(arr):
    n=len(arr)

    for i in range(n-1):
        
        for j in range(n-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
        
    print(arr)
arr=[1,6,2,7,2,5,0]
bubblesort(arr)