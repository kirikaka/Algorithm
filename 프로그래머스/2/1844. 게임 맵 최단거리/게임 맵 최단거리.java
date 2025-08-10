import java.util.*;

class Solution {
    private final int[] dx={-1,1,0,0};
    private final int[] dy={0,0,1,-1};
    
    
    public int solution(int[][] maps) {
        int n=maps.length;
        int m=maps[0].length;
        
        int[][]dist=new int[n][m];
        boolean[][]visited=new boolean[n][m];
        
        ArrayDeque<int[]>que=new ArrayDeque<>();
        que.offer(new int[]{0,0});
        dist[0][0]=1;
        visited[0][0]=true;
        
        while(!que.isEmpty()){
            int[] cur=que.poll();
            int x=cur[0],y=cur[1];
            
            if(x==n-1&&y==m-1){
                return dist[x][y];
            }
            
            for(int i=0;i<4;i++){
                int nx=x+dx[i];
                int ny=y+dy[i];
                
                if(nx>=0 && nx<n && ny>=0 && ny<m){
                    if(!visited[nx][ny] && maps[nx][ny]==1){
                        visited[nx][ny]=true;
                        dist[nx][ny]=dist[x][y]+1;
                        que.offer(new int[]{nx,ny});
                    }
                }
            }
            
        }
        
        
        
        return -1;
    }
}