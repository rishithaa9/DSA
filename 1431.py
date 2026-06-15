class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_kid=max(candies)
        print(max_kid)
        result=[0]*len(candies)
        for i in range(len(candies)):
            sumc=candies[i]+extraCandies
            if sumc>=max_kid:
                result[i]=True
            else:
                result[i]=False       
        return result