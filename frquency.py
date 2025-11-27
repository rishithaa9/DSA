def frequency(s):
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for j in count:
        print(j,count[j])
        
frequency(s="abcdabcde")
            
    