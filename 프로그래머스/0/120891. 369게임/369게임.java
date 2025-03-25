class Solution {
    public int solution(int order) {
        String ordes=order+"";
        String[] orders=ordes.split("");
        int answer=0;
        
        for(String s : orders){
            if(s.equals("3") || s.equals("6") || s.equals("9") ) answer++;
        }
        
        
        return answer;
    }
}