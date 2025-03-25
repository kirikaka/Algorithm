import java.util.*;

class Solution {
    public String solution(String letter) {
        String answer = "";
        
        String[] morseCode = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        
        Map<String, Character> morse = new HashMap<>();
        
        for (int i = 0; i < alphabet.length(); i++) {
            morse.put(morseCode[i], alphabet.charAt(i));
        }
    
        String[] ans=letter.split(" ");
        for(int i=0;i<ans.length;i++){
            answer=answer+morse.get(ans[i]);
        }
        
    
        
        
        
        return answer;
    }
}