class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window=[]
        left=0
        res=[]
        window=nums[0:k]
        max_val=max(window)
        res.append(max_val)
        print(res)
        for right in range(k,len(nums)):
            window.append(nums[right])
            res.append(max(window))
            window.remove(nums[left])
            left+=1
        return res
        