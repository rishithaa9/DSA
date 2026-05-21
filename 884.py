class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count={}
        result = []
        for i in s1.split():
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for i in s2.split():
            if i not in count:
                count[i]=1
            else:
                count[i]+=1

        for key,val in count.items():
            if val < 2:
                result.append(key)
        return result 


        