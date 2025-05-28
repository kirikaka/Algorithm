import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        
        int n=maps.length;
        int m=maps[0].length;
        
        boolean[][] visited=new boolean[n+1][m+1];
        
        ArrayDeque<Integer[]> queue= new ArrayDeque<>();
        queue.add(new Integer[]{0,0,1});
        visited[0][0]=true;
        
        int[] dr={0,0,-1,1};
        int[] dc={1,-1,0,0};
        
        while(!queue.isEmpty()){
            Integer []cur=queue.poll();
            int curRow=cur[0];
            int curCol=cur[1];
            int curDist=cur[2];
            if(curRow==n-1&&curCol==m-1){
                answer=curDist;
                break;
            }
            
            
            for(int i=0;i<4;i++){
                int nextRow=dr[i]+curRow;
                int nextCol=dc[i]+curCol;
                int nextDist=curDist+1;
                if(nextRow>=0 && nextRow<n && nextCol>=0 && nextCol<m){
                    if(!visited[nextRow][nextCol] && maps[nextRow][nextCol]==1){
                        queue.offer(new Integer[]{nextRow,nextCol,nextDist});
                        visited[nextRow][nextCol]=true;
                    }
                }
                
                
            }
            
            
            
        }
        
        
        
        return answer;
    }
}