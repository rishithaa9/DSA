class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count={}
        for i in text:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )

        