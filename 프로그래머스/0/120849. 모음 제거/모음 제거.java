class Solution {
    public String solution(String my_string) {
        String answer = "";
        String moum="aeiou";
        
        
        for(int i=0;i<my_string.length();i++){
            String temp="";
            temp=temp+my_string.charAt(i);
            if (moum.contains(temp)){
                continue;
            } else{
                answer+=temp;
            }
        }
        
        
        return answer;
    }
}