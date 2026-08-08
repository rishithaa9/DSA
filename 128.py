class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        max_length=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                current=i
                length=1
            while current+1 in nums:
                length+=1
                current=current+1
            max_length=max(max_length,length)
        return max_length


        
        