class Solution {
    public int solution(int[] array, int n) {
        int answer = array[0];
        int x=(n-array[0])*(n-array[0]);
        int tmp=0;
        
        for (int i=1;i<array.length;i++){
            tmp=(n-array[i])*(n-array[i]);
            
            if (tmp<x) {
                x=tmp;
                answer=array[i];
            } else if(tmp==x){
                answer=(answer>array[i]) ? array[i] : answer;
            }
            
        }
        
        return answer;
    }
}