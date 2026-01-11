class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count={}
    
        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        max_value=-1
        for i,freq in count.items():
            if i==freq:
                max_value=max(i,max_value) 
        return max_value
            
