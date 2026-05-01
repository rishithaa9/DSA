import math 
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_v=0
        mxi=[]
        result=0 
        n=len(nums)
        left =0 
        right = len(nums) -1
        for i in range(len(nums)):
            max_v=max(max_v,nums[i])
            mxi.append(max_v)
        prefixgod=[]
        for i in range(n):
            prefixgod.append(math.gcd(nums[i],mxi[i]))
        prefixgod.sort()
        while left < right : 
            a=prefixgod[left]
            b=prefixgod[right]
            left+=1
            right-=1   
            result+=math.gcd(a,b)
        return result
        
            


        
        