class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr=[0] * len(nums)
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] :
                    arr[i]+=abs(i-j)
        return arr

            