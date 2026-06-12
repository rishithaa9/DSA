class Solution {
    public void sortColors(int[] nums) {
        int n=nums.length;
        int left=0;
        int mid=0;
        int right=n-1;

        while (mid<=right){
            if (nums[mid]==1){
                mid=mid+1;
            }
            else if (nums[mid]==0){
                int temp=0;
                temp=nums[left];
                nums[left]=nums[mid];
                nums[mid]=temp;
                mid=mid+1;
                left++;
            }
            else{
                int temp=0;
                temp=nums[right];
                nums[right]=nums[mid];
                nums[mid]=temp;
                right--;
            }

        }
        
    }
}