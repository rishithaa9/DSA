import java.util.HashMap;

class Solution {
    public boolean isGood(int[] nums) {
        HashMap<Integer,Integer> count=new HashMap<>();
        int n=nums.length;
        int max_num=nums[0];

        for(int i:nums){
            max_num=Math.max(i,max_num);
        }
        for(int i:nums){
            count.put(i,count.getOrDefault(i,0)+1);
        }
        for(int i=1;i<max_num+1;i++){
            int freq=count.getOrDefault(i,0);
            if (i==max_num){
                if (freq!=2){
                    return false;
                }
            }
            else{
                if (freq!=1){
                    return false;
                }
                
            }
        }
        return true;
        
    }

}