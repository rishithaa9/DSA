class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count=0
        result=[]
        n=len(A)
        freq=[0] * (n+1)
        for i in range(n):
            freq[A[i]]+=1
            if freq[A[i]]==2:
                count+=1
            freq[B[i]]+=1
            if freq[B[i]]==2:
                count+=1
            result.append(count)
        return result