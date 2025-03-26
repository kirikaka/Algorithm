import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int rem=0;
        
        String[] sik=s.split(" ");
        // System.out.println(sik);
        
        for(String temp:sik){
            if (temp.equals("Z")){
                answer-=rem;
            }
            else{
                answer+=Integer.parseInt(temp);
                rem=Integer.parseInt(temp);
            }
        }
        
        
        
        return answer;
    }
}

// Integer.parseInt