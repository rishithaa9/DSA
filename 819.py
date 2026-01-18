class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        banned=set(banned)
        for ch in "!?',;.":
            paragraph=paragraph.replace(ch," ")
        paragraph=paragraph.split()
        count={}
        for ch in paragraph:
            if ch not in banned:
                count[ch]=count.get(ch,0)+1

        return max(count,key=count.get)



