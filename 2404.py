class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count={}
        result=-1

        for i in nums:
            if i%2 ==0:
                if i not in count:
                    count[i]=1
                else:
                    count[i]+=1
        max_val=0
        for key,val in count.items():
            if val>max_val:
                max_val=val
                result=key

            elif val == max_val and key <result :
                result=key

        return result
            