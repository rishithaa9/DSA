def linear(arr,tar,i):
    if len(arr)==i:
        return False
    if arr[i]==tar:
        return True
    return linear(arr,tar,i+1)