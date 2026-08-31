class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left=0
        count={}
        max_len=0
        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]]=1
            else:
                count[s[right]]+=1

            while count[s[right]]>2:
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len

        