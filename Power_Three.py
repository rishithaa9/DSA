class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        while 3**i<=n:
            if n==3**i:
                
                return True
            i+=1
        return False
        