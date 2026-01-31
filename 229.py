#229
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        result = []
        for key,value in count.items():
            if value > len(nums) // 3:
                result.append(key)
        return result

        