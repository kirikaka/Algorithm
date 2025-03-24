class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        String nums=Integer.toString(num);
        char need=Integer.toString(k).charAt(0);
        
        for(int i=0;i<nums.length();i++){
            if(need==nums.charAt(i)){
                answer= i+1;
                break;
            }
        }
        if (answer==0){
            return -1;
        } else{
            return answer;
        }
        
        
    }
}