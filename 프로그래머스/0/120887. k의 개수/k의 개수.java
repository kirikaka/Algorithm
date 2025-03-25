class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        char need='a';
        char[] tmp;        
        
        for(int x=i;x<=j;x++){
            need=(char)(k+'0');
            tmp=(x+"").toCharArray();
            for(char c:tmp){
                if(need==c) answer++;
            }
            
        }
        
        
        return answer;
    }
}