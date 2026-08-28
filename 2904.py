class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        counto=0
        res=""
        for right in range(len(s)):
            if s[right]=="1":
                counto+=1
            while counto>k:
                if s[left]=="1":
                    counto-=1
                left+=1

            if counto==k:
                while s[left]=="0":
                    left+=1
                can=s[left:right+1]
                if (res=="" or len(can) < len(res) or (len(can)==len(res) and can <res)):
                    res=can
        return res

            
        