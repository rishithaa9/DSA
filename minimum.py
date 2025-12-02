def minimum(a):
    product=[]
    min_value=float('inf')
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            product=a[i]*a[j]
            if product<min_value:
                min_value=product
                
    print(min_value)
minimum([1,3,4,7])