class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        lower=set()
        upper=set()
        for i in word:
            if i.islower():
                lower.add(i)
            else:
                upper.add(i)

        for i in lower:
            if i.upper() in upper:
                count+=1
        return count 