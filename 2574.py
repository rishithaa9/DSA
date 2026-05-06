class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0] * len(nums)

        rightsum=[0] * len(nums)
        rightsum[-1]=0
        res=[]
        for i in range(len(nums)-1):
            leftsum[i+1]=leftsum[i]+nums[i]
        for i in range(len(nums)-2, -1, -1):
            rightsum[i]=rightsum[i+1]+nums[i+1]
        for i in range(len(nums)):
            res.append(abs(leftsum[i]-rightsum[i]))
        return res
        
        