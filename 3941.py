class Solution:
    def passwordStrength(self, password: str) -> int:
        count=0
        passs=set(password)
        for ch in passs:
            if ch.islower():
                count+=1
            elif ch.isupper():
                count+=2
            elif ch.isdigit():
                count+=3
            else:
                count+=5
        return count 

        