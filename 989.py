class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numw=0
        for i in num:
            numw=numw* 10 + i

        numw=numw+k 
        res=[]
        for j in str(numw):
            res.append(int(j))
        return res

        