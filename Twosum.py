def twosum(a,target):
    n=len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j]==target:
                print(a[i],a[j])
                
    
arr=[2,7,2,3,4,5]
target=9
twosum(arr,target)