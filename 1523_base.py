class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result=[]

        for i in range(low,high+1):
            result.append(i)
        count=0
        print(result)
        for i in result:
            if i%2==1:
                count+=1
        return count 