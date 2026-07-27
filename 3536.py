class Solution:
    def maxProduct(self, n: int) -> int:
        product=0
        max_p=0
        n=str(n)
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                product=int(n[i])*int(n[j])
                max_p=max(max_p,product)

        return max_p
            
        