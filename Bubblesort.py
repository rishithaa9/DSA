def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break

if __name__=="__main__":
    arr=[9,3,1,0,4]
    print('original array',arr)
    bubblesort(arr)
    print('sorted array:',arr)