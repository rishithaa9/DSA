class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count={}
        for x in nums:
            if x not in count:
                count[x]=1
            else:
                count[x]+=1
            

        max_num=max(nums)

        ans=1
        if 1 in count:
            if count[1]%2==0:
                ans=count[1]-1
            else:
                ans=count[1]

        for x in list(count.keys()):
            if x==1:
                continue
            
            curr=x
            length=0
            while curr<=max_num and count.get(curr,0)>=2:
                length+=2
                curr*=curr
            if count.get(curr,0):
                length+=1
            else:
                length-=1
            ans=max(ans,length)
        return ans

        