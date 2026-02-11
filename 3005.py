class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        result=0
        max_count=0

        for key,value in count.items():
            if value > max_count:
                max_count=value
                result=value

            elif value==max_count:
                result+=value

        return result
        