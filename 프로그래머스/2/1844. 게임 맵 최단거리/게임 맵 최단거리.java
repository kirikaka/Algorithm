import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        
        int n=maps.length;
        int m=maps[0].length;
        
        Queue<int[]>queue=new ArrayDeque<>();
        boolean[][] visited=new boolean[n][m];
        
        queue.add(new int[]{0,0,1});
        visited[0][0]=true;
        
        int[] dr={-1,1,0,0};
        int[] dc={0,0,1,-1};
        
        while(!queue.isEmpty()){
            int[] curr=queue.poll();
            int curR=curr[0];
            int curC=curr[1];
            int curDis=curr[2];
            
            if(curR==n-1 && curC==m-1){
                answer=curDis;
            }
            
            for(int i=0;i<4;i++){
                int nextR=curR+dr[i];
                int nextC=curC+dc[i];
                if(nextR>=0 && nextC>=0 && nextR<n && nextC<m){
                    if(!visited[nextR][nextC] && maps[nextR][nextC]==1){
                        visited[nextR][nextC]=true;
                        queue.offer(new int[]{nextR,nextC,curDis+1});
                    }
                }
            }
            
        }
        
        
        return answer;
    }
}