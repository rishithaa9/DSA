#Count subarrays of size k whose sum is even
def max_sum(arr,k):
    n=len(arr)
    window_state=0
    count=0
    
    for i in range(k):
        window_state+=arr[i]
    if window_state % 2 == 0:
        count+=1
    for i in range(k,n):
        window_state+=arr[i]
        window_state-=arr[i-k]
        
        if window_state%2 ==0:
            count+=1
            
    return count 
    
print(max_sum([2,3,4,6,1], 2))