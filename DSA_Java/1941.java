class Solution {
    public boolean areOccurrencesEqual(String s) {
            HashMap<Character,Integer>map=new HashMap<>();
        for (char x:s.toCharArray()){
            map.put(x,map.getOrDefault(x,0)+1);
        }
        int freq=-1;
        for (Map.Entry<Character,Integer> entry: map.entrySet()) {
            int val=entry.getValue();
            if(freq == -1){
                freq = val;
            }
            else if(freq != val){
                return false;
            }
        }
        return true;   
    }
    public Solution() {
    }
}