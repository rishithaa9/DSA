def subarr(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
subarr(arr=[1,2,4,5,6,6])