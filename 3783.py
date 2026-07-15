class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        x=n
        results=0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        rev =rev
        results= abs(n-rev)
        return results

        
        