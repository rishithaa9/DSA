class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> countofs=new HashMap<>();
        HashMap<Character,Integer> countoft=new HashMap<>();

        for (char x:s.toCharArray()){
            countofs.put(x,countofs.getOrDefault(x,0)+1);
        }
        for (char x:t.toCharArray()){
            countoft.put(x,countoft.getOrDefault(x,0)+1);
        }
        return countofs.equals(countoft);

    }
}