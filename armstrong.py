def armstrong(s):
    lenn=len(str(s))
    n=0
    sum=0
    while lenn>0:
        n= n % 10 
        sum+=n * lenn
        n=n//10
    print(sum)
    if sum==s:
        print("True")
    print("False") 
        
n=153
armstrong(n)
