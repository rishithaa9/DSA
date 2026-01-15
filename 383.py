class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count={}

        for i in magazine:
            count[i]=count.get(i,0)+1

        for i in ransomNote:
            if count.get(i,0)==0:
                return False
            count[i]-=1
        return True
        