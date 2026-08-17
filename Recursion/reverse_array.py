def reverse_array(arr):
    def solve(left,right):
        if left>=right:
            return 
    
        
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

        solve(left,right)
    solve(0,len(arr)-1)
    return arr

arr=[5,4,3,2,1]
print(reverse_array(arr))