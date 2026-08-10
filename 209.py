class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_length = float('inf')
        sum_a=0
        for right in range(len(nums)):
            sum_a+=nums[right]
            while sum_a>=target:
                min_length=min(min_length,right-left+1)
                sum_a-=nums[left]
                left+=1
        if min_length==float('inf'):
            return 0
        else:
            return min_length