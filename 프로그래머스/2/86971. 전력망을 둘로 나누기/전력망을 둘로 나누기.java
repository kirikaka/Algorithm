import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        ArrayList[] graph=new ArrayList[n+1];
        for(int i=1;i<=n;i++){
            graph[i]=new ArrayList<>();
            System.out.println(graph[i]);
        }
        for(int []wire:wires){
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }
        
        for(int[] wire : wires){
            int a=wire[0];
            int b=wire[1];
            graph[a].remove(Integer.valueOf(b));
            graph[b].remove(Integer.valueOf(a));
            
            int count=1;
            boolean[] visited=new boolean[n+1];
            ArrayDeque<Integer>queue=new ArrayDeque<>();
            queue.add(a);
            
            visited[a]=true;
            
            while(!queue.isEmpty()){
                int cur=queue.poll();
                ArrayList<Integer> nexts = graph[cur];
                for(int next : nexts){
                    if(!visited[next]){
                        visited[next]=true;
                        count++;
                        queue.add(next);
                    }
                }
            }
            int count2=n-count;
            answer=Math.min(answer,Math.abs(count2-count));
            
            graph[a].add(b);
            graph[b].add(a);
            
            
        }
        
        
        return answer;
    }
}