class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        news=s+s 
        if len(s)!=len(goal):
            return False
        else:
            if goal in news:
                return True 
            return False 
        