class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        if len(set(count.values()))==1:
            return True
        return False
        