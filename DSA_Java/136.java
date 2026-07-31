class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> map= new HashMap<>();
        for(int x: nums){
            map.put(x,map.getOrDefault(x,0)+1);

        }
        int res=0;
        for(Map.Entry<Integer,Integer> entry:map.entrySet()){
            int key=entry.getKey();
            int val=entry.getValue();

            if (val!=2){
                res=key;
            }
        }
        return res;
        
    }
}