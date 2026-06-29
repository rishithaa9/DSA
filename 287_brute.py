class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
        for key,val in count.items():
            if val>=2:
                return key
        