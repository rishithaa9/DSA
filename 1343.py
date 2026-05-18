class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)

        window=sum(arr[:k])
        count=0
        if window>=(k* threshold):
            count+=1
        for i in range(k,n):
            window=window+arr[i]-arr[i-k]

            if window >= (k*threshold):
                count+=1
        return count 
            