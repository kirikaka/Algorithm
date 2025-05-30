import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        
        int rowLength=maps.length;
        int colLength=maps[0].length;
        
        boolean[][] visited=new boolean[rowLength+1][colLength+1];
        ArrayDeque<int[]> queue=new ArrayDeque<>();
        
        queue.add(new int[]{0,0,1});
        visited[0][0]=true;
        int[] dr={-1,1,0,0};
        int[] dc={0,0,1,-1};
        
        while(!queue.isEmpty()){
            int []cur=queue.poll();
            
            int curRow=cur[0];
            int curCol=cur[1];
            int curDist=cur[2];
            
            if(curRow==rowLength-1 && curCol==colLength-1){
                return curDist;
            }
            
            
            for(int i=0;i<4;i++){
                int nextRow=curRow+dr[i];
                int nextCol=curCol+dc[i];
                
                
                if(nextRow>=0 && nextRow<rowLength && nextCol>=0 && nextCol<colLength){
                    if(!visited[nextRow][nextCol] && maps[nextRow][nextCol]==1){
                        queue.add(new int[]{nextRow,nextCol,curDist+1});
                        visited[nextRow][nextCol]=true;
                    }
                }
                
            }
            
        }
        
        
        
        return answer;
    }
}