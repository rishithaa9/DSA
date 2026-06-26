class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count=0
        ans=0
        length=0
        for i in range(len(nums)):
            targetCount = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    targetCount += 1
                length = j - i + 1
                if targetCount > length // 2:
                    ans += 1
        return ans
        