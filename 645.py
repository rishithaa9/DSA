    class Solution:
        def findErrorNums(self, nums: List[int]) -> List[int]:
            arr=[]
            res={}
            missing=0
            result=[]
            numset=set(nums)
            for i in range(1,len(nums)+1):
                arr.append(i)
            for i in arr:
                if i not in numset:
                    missing=i
            for i in nums:
                if i not in res:
                    res[i]=1
                else:
                    res[i]+=1
            for key,val in res.items():
                if val > 1:
                    result.append(key)
            result.append(missing)
            return result
                    
            

            