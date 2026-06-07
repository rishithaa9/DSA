class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        p=[]
        for i in l:
            p.append(i[::-1])
        return ' '.join(p)


        