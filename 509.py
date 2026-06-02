class Solution:
    def fib(self, n: int) -> int:
        a=n-1
        b=n-2
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
        


        