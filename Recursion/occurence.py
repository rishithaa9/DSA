def occurence(arr,tar,i):
    if len(arr)==i:
        return -1
    if arr[i]==tar:
        return i
    return occurence(arr,tar,len(arr)-1)

    #R11