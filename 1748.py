class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]=count.get(i,0)+1
            else:
                count[i]=1
        add=0
        for i,freq in count.items():
            if freq==1:
                add+=i
        return add

        
        