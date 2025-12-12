class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        hash={}

        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]]+=1

            else:
                hash[nums[i]]=1


                

        