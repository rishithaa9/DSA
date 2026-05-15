class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count={}
        for i in nums:
            for j in set(i):
                if j not in count:
                    count[j]=1
                else:
                    count[j]+=1
        result=[]
        for key,val in count.items():
            if val==len(nums):
                result.append(key)
        return sorted(result)
                



        