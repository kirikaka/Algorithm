import java.util.*;

class Solution {
    boolean openBracket(char bracket){
        if(bracket=='(' || bracket=='['||bracket=='{' ){ 
            return true;
        } else{
            return false;
        }
        
    }
    boolean matchBracket(char open,char close){
        if( open=='(' && close==')'){
            return true;
        }
        if( open=='{' && close=='}'){
            return true;
        }
        if( open=='[' && close==']'){
            return true;
        }
        return false;
    }
    
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character>bracket=new Stack<>();
        
        for(int i=0;i<s.length();i++){
            char curBracket=s.charAt(i);
            if(openBracket(curBracket)){
                bracket.push(curBracket);
            } else{
                if(bracket.isEmpty()) {
                    System.out.println("이게 문제1?");
                    return false;
                };
                char lastBracket=bracket.pop();
                if(!matchBracket(lastBracket,curBracket)){
                    System.out.println("이게 문제2?");
                    return false;
                }
                
            }
        }
        if(!bracket.isEmpty()) return false;
        

        return answer;
    }
}