class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] sik=my_string.split(" ");
        boolean min=false;
        
        for(String s:sik){
            if(s.equals("-")){
                min=true;
                
            }else if(s.equals("+")){
                min=false;
            }else{
                if(min){
                    answer-=Integer.parseInt(s);
                }
                else{
                    answer+=Integer.parseInt(s);
                }
            };
                
        }
        
        
        return answer;
    }
}