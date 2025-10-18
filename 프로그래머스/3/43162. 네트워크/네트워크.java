import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[]visited = new boolean[n];
        
        for(int i=0;i<n;i++){
            if(visited[i]) continue;
            bfs(n,computers,visited,i);
            answer++;
        }
        
        return answer;
    }
    
    void bfs(int n,int[][] computers,boolean[] visited,int start){
        Queue<Integer>queue=new LinkedList<>();
        queue.offer(start);
        visited[start] =true;
        
        while(!queue.isEmpty()){
            int cur=queue.poll();
            for(int i=0;i<n;i++){
                if(!visited[i] && computers[cur][i]==1){
                    queue.offer(i);
                    visited[i]=true;
                }
            }
            
        }
        
    }
} 