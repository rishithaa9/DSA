class Solution:
    def sumAndMultiply(self, n: int) -> int:
        xx=[]
        summ=0
        for x in str(n):
            if x!='0':
                xx.append(x)
                summ+=int(x)
        if not xx:
            return 0
        number = int("".join(xx))
        return number*summ

        