class Solution:
    def secondHighest(self, s: str) -> int:
        
        nums = []

        for ch in s:
            if ch.isdigit():
                nums.append(int(ch))
        nums=list(set(nums))
        nums.sort()
        if len(nums)> 1:
            return nums[-2]
        return -1 