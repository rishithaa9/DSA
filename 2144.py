class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total=0
        sor=sorted(cost,reverse=True)
        for i in range(0,len(sor),3):
            total+=sor[i]
            if i+1 < len(sor):
                total+=sor[i+1]

        return total




            
        