class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr+=nums[j]
                if curr==k:
                    count+=1

        return count 

        