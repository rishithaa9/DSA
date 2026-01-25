class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1={}
        count2={}
        for i in words1:
            if i in count1:
                count1[i]=count1.get(i,0)+1
            else:
                count1[i]=1
        for j in words2:
            if j in count2:
                count2[j]=count2.get(j,0)+1
            else:
                count2[j]=1

        ans=0
        for i,freq in count1.items():
            if freq==1 and count2.get(i,0)==1:
                ans+=1
        return ans 
            



            