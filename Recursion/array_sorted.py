def arrissorted(arr,n):
    if n==1 or n==0:
        return True
    if arr[n-2]>arr[n-1]:
        return False

    return arrissorted(arr,n-1)
