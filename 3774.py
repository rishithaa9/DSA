class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        small = sum(nums[:k])
        large = sum(nums[-k:])
        
        return large - small