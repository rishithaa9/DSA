class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        count={}
        for i in str(n):
            if i in count:
                count[i]=count.get(i,0)+1
            else:
                count[i]=1

        min_value=float('inf')
        ans=float('inf')
        for i,frq in count.items():
            if frq< min_value:
                min_value=frq
                ans=int(i)
            elif frq==min_value:
                ans=min(ans,int(i))
        return ans



        
         
        