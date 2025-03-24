import java.util.*;

class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        char[] arr=my_string.toCharArray();
        
        char temp1=arr[num1];
        arr[num1]=arr[num2];
        arr[num2]=temp1;
        
        
        answer=new String(arr);
        
        return answer;
    }
}