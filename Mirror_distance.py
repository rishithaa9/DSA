#3783
class Solution:
    def mirrorDistance(self, n: int) -> int:
        s=n
        rev=0
        while n>0:
            digit=n%10
            rev=(rev*10)+digit
            n=n//10
        
        distance=abs(s-rev)
        return distance
        