class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"

        count={}
        for ch in s:
            if ch not in count:
                count[ch]=1
            else:
                count[ch]+=1
        max_vowels=0
        max_conso=0
        for key,val in count.items():
            if key in vowels: 
                max_vowels=max(max_vowels,val)
            else:
                max_conso=max(max_conso,val)
        return max_vowels+ max_conso

               