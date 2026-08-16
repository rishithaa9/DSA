def palindrome_twopointers(s):
    left=0
    right=len(s)-1

    if s[left]!=s[right]:
        return False
    elif left>=right:
        return True
    else:
        left+=1
        right-=1
        return palindrome_twopointers(s[left:right+1])