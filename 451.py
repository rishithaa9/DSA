class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_i=""
        count={}
        for ch in s:
            if ch not in count:
                count[ch]=1
            else:
                count[ch]+=1
        count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        for key,val in count:
            sorted_i+=key * val
        return sorted_i
            

        