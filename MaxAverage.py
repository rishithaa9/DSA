class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        max_sum=0
        window_state=0
        for i in range(k):
            window_state+=nums[i]
            
        max_sum=window_state

        for i in range(k,n):
            window_state+=(nums[i])
            window_state-=(nums[i-k])
            max_sum=max(max_sum,window_state)

        return max_sum/k

        