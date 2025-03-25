class Solution {
    public int[][] solution(int[] num_list, int n) {
        
        
        int[][] answer = new int[num_list.length/n][n];
        for(int i=0;i<num_list.length/n;i++){
            for(int j=0;j<n;j++){     
                int place=i*n+j;
                answer[i][j]=num_list[place];
            }
        }
        
        return answer;
    }
}