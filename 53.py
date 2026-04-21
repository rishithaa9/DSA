class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxs=float('-inf')
        sum=0
        for i in nums:
            sum+=i
            maxs=max(maxs,sum)
            if sum<0:
                sum=0
        return maxs 
        