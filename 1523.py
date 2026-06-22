class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #count=[]
        #for i in range(low,high+1):
        #   if i%2==1:
        #       count.append(i)

        #return len(count)
        return (high+1) //2 - low // 2 