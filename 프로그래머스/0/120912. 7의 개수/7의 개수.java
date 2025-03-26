class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int len=array.length;
        String seven="";
        
        for(int i=0;i<len;i++){
            seven+=array[i]+"";
            
        }
        seven=seven.replaceAll("[^7]","");
        
        
        
        return seven.length();
    }
}