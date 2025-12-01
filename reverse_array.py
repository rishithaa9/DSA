def remove(a):
    n=len(a)
    left=0
    right=n-1
    while left<right:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1
    print(a)
A = [1, 2, 3, 4, 5]
remove(A)