class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        P = [[0] * (n+1) for _ in range(m+1)]
        ans=[[0]*n for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                P[i][j]=mat[i-1][j-1]+P[i-1][j]+P[i][j-1]-P[i-1][j-1]
        for i in range(m):
            for j in range(n):
                r1=max(0,i-k)
                c1=max(0,j-k)
                r2=min(m-1,i+k)
                c2=min(n-1,j+k)
                ans[i][j]=P[r2+1][c2+1]-P[r1][c2+1]-P[r2+1][c1]+P[r1][c1]
        return ans
