class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        i=0
        j=n-1
        max_dis=0
        ans=0
        for j in range(n-1,-1,-1):
            if colors[j]!=colors[0]:
                max_dis=j
                
                break
        for i in range(n):
            if colors[i]!=colors[n-1]:
                max_dis = max(max_dis,n-1-i)
                break

        return max(max_dis,ans)


        