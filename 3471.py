class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        max_val=0
        value=[]
        left=0
        count={}
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            for num in set(window):
                count[num] = count.get(num, 0) + 1
        for key,val in count.items():
            if val==1:
                value.append(key)

        return max(value) if value else -1


        

            

        