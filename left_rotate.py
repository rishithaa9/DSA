def move_zeros(arr):
    temp=arr[0]
    n=len(arr)
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    print(arr)
arr=[0,10,3,12]
move_zeros(arr)

