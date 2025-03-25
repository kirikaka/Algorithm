import java.util.*;

class Solution {
    public int solution(String before, String after) {
        int answer = 1;
        char[] before_s=before.toCharArray();
        char[] after_s=after.toCharArray();
        Arrays.sort(before_s);
        Arrays.sort(after_s);
        
        for(int i=0;i<after.length();i++){
            if(before_s[i]!=after_s[i]) answer=0;
        }
        
        
        return answer;
    }
}