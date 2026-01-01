#414
def maxSubArray(nums) -> int:
    sum=0
    max=0
    n=len(nums)
    for i in range(n):
        for j in range(1,n):
            sum=nums[i]+nums[j]
            if sum>max:
                max=sum
    return max

print(maxSubArray([5,4,-1,7,8]))