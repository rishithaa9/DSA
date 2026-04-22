def selectionsort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i,n):
            if arr[j]<arr[min_index]:
                arr[j],arr[min_index]=arr[min_index],arr[j]

    print(arr)
arr=[1,6,2,7,3,5,1]
selectionsort(arr)