class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        res=n
        ans=0
        while res>=n:
            prod=1
            for i in str(res):
                prod*=int(i)
            if prod%t==0:
                return res
            else:
                res=res+1




        
        