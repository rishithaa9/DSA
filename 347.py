class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1

        count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(count[i][0])
        return result
