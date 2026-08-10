class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
    def atMost(self,nums, goal):
        if goal<0:
            return 0
        left=0
        max_w=0
        curr_sum=0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>goal:
                curr_sum-=nums[left]

                left+=1
            max_w+=right-left+1
        return max_w
        