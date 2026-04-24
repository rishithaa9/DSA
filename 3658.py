class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
    
        sumeven= n *( n+1)
        sumodd=n * n

        temp=0
        while sumeven!=0:
            temp=sumeven
            sumeven=sumodd%sumeven
            sumodd=temp
        return sumodd 
