class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_occ():
            left=0
            right=len(nums)-1
            pos=-1
            while left<=right:
                mid= (left + right) // 2 
                if nums[mid]==target:
                    pos=mid
                    right=mid-1
                elif nums[mid] < target :
                    left=mid+1
                else:
                    right=mid-1
            return pos


        def Last_occ():
            left=0
            right=len(nums)-1
            pos=-1
            while left<=right:
                mid= ( left + right ) //  2
                if nums[mid]==target:
                    pos=mid
                    left=mid+1
                    
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1 
            return pos
        return [first_occ(),Last_occ()]

