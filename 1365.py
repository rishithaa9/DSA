class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                smaller=0
                for j in nums:
                    if i >j :
                        smaller+=1
                count[i]=smaller
        result=[]
        for num in nums:
            result.append(count[num])
        return result