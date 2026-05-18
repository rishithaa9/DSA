class Solution {
    public double findMaxAverage(int[] nums, int k) {
        n=nums.length;
        if n <k return -1;
        int window=Math.sum(nums,0,k-1);
        int result=window;
        for (int i=k;i<=n;i++){
            window=window+nums[i]-nums[i-k];
            result=Math.max(result,window);
        }
        return (double)result/k;
        
    }
}