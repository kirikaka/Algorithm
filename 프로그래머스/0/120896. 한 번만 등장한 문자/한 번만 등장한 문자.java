import java.util.*;


class Solution {
    public String solution(String s) {
        String answer="";
        
        for(String sc:s.split("")){
            if(s.indexOf(sc)==s.lastIndexOf(sc)){
                answer+=sc+"";
            }
        }
        System.out.println(answer);
        char[] c=answer.toCharArray();
        Arrays.sort(c);
        
        
        String ans=new String(c);
        
        
        
        return ans;
    }
}