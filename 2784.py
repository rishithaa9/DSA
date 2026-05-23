class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count={}
        n=len(nums)
        max_n=max(nums)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for i in range(1,max_n+1):
            freq=count.get(i,0)
            if i==max_n:
                if freq!=2:
                    return False
            else:
                if freq!=1:
                    return False
        return True
 
                
        
        