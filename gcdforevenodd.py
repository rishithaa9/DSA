class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = []
        odd = []
        sumeven=0
        sumodd=0
        for i in range(1,n+1):
            even.append(2*i)
        for i in range(n):
            odd.append(2*i + 1)
        print("Even:", even)
        print("Odd:", odd)
        for i in range(len(even)):
            sumeven+=even[i]
        for i in range(len(odd)):
            sumodd+=odd[i]

        temp=0
        while sumeven!=0:
            temp=sumeven
            sumeven=sumodd%sumeven
            sumodd=temp
        return sumodd 

 