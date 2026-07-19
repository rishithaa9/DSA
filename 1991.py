class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ls=[0]*n
        rs=[0] *n
        for i in range(n):
            ls[i]=ls[i-1]+nums[i]

        rs[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            rs[i]=rs[i+1]+nums[i]
        for i in range(n):
            if ls[i]==rs[i]:
                return i
        return -1 
        
        
        