class Solution:
    def isValid(self, s: str) -> bool:
        ss={'}':'{',')':'(',']':'['}
        stack=[]
        for i in s:
            if i in ss.values():
                stack.append(i)
            elif i in ss:
                if not stack or ss[i]!=stack.pop():
                    return False
        return not stack