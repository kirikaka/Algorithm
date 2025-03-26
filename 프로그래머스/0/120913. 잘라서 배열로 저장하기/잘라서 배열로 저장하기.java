class Solution {
    public String[] solution(String my_str, int n) {
        
        int len=0;
        if(my_str.length()%n==0){
            len=my_str.length()/n;
        } else{
            len=my_str.length()/n+1;
        }
        String[] answer = new String[len];
        for(int i=0;i<len;i++){
            if( (i+1)*n>my_str.length()){
                answer[i]=my_str.substring(i*n,my_str.length());
            } else{
                answer[i]=my_str.substring(i*n,(i+1)*n);
            }
        }
        
        
        return answer;
    }
}