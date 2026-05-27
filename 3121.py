class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low={}
        up={}
        count=0
        for i in range(len(word)):
            if word[i].islower():
                low[word[i]]=i
            else:
                up[word[i]]=i
        for i in low:
            if i.upper() in up: 
                if low[i] < up[i.upper()]:
                    count += 1
        return count 

        
        