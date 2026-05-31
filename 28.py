class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n=len(haystack) - len(needle) 
        for i in range(n+1):
            if haystack[i:i+len(needle)]== needle:
                return i
        return -1

        