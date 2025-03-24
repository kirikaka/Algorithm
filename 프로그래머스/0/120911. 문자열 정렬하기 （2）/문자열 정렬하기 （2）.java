import java.util.*;

class Solution {
    public String solution(String my_string) {
        char[] c=my_string.toLowerCase().toCharArray();
        
        Arrays.sort(c);
        String answer =new String(c);
        
        return answer;
    }
}