class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split()
        count=0
        for word in words:
            bad=False
            for ch in word:
                if ch in brokenLetters:
                    bad=True
                    break
            if not bad: 
                count+=1
        return count
        