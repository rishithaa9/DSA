class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for i in nums:
            if i >0 :
                pos.append(i)
            else:
                neg.append(i)

        nums1=[]
        j=0
        for i in range(len(pos)):
            nums1.append(pos[i])
            nums1.append(neg[j])
            j+=1
        return nums1

                
        