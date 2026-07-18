class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        summ =0
        for i in range(rows):
            summ+= mat[i][i]
            summ+=mat[i][rows-1-i]
        if rows%2 ==1 :
            summ-=mat[rows//2][rows//2]
        return summ

        