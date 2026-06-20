class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        equal=[]
        greater=[]

        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                less.append(i)

        return (less+equal+greater)
        