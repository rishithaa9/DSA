def anagram(s,t):
    if(len(s)!=len(t)):
        return False
    counts={}
    for ch in s:
        counts.get(ch,0)+1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch]-=1
        if ch in counts<0:
            return False
    return True

    