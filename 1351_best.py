class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])

        i=0
        j=cols-1
        while i<rows and j>=0:

                if grid[i][j]<0:
                    count+=(rows-i)
                    j-=1
                else:
                    i+=1
        return count
        