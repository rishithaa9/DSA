class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        ans=[]
        for i in range(1,len(nums)+1):
            result.append(i)
        
        for i in result:
            if i not in nums:
                ans.append(i)
        return ans

        