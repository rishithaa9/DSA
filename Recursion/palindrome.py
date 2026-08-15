def palindrome(s):

    if len(s)==0:
        return True

    if len(s)==1:
        return True

    return palindrome(s[1:-1]) and s[0]==s[-1]