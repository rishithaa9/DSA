def fib(n):
    if n<=1:
        return n
    if n>1:
        return fib(n-1)+fib(n-2)
    

n=6
print(fib(int(n)))