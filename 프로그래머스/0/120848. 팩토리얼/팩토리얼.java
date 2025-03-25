class Solution {
    public int solution(int n) {
        int answer = 1;
        while(true){
            int sum=1;
            for(int i=1;i<=answer;i++){
                sum=sum*i;
            }
            if(sum>n) return answer-1;
            else answer++;
        }
        
        
    }
}