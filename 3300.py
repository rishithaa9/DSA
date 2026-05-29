class Solution:
    def minElement(self, nums: List[int]) -> int:

        dig=0
        min_dig=float('inf')
        for num in nums:
            for i in str(num):
                dig+=int(i)
                
            min_dig=min(dig,min_dig)
            dig=0
            
        return min_dig

        