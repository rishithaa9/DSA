def reverrse_integer(n):
    if n==0:
        return

    print(n%10)
    reverrse_integer(n//10)
reverrse_integer(12345)

#R6