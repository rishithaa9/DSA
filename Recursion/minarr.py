def mina(arr,i):
    if i==len(arr)-1:
        return arr[i]

    re=mina(arr,i+1)
    return min(arr[i],re)