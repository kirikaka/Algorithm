import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        // 모든 입력된 전선을 순회하며 끊었다 붙여가며 갯수를 센다.
        ArrayList<Integer>[] graph=new ArrayList[n+1];
        for(int i=1;i<=n;i++){
            graph[i]=new ArrayList<>();
        }
        for(int []wire : wires){
            // graph만들기
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
            
        }
        // 전선 끊어서 길이 확인
        int max=0;
        for(int[] wire:wires){
            int a=wire[0];
            int b=wire[1];
            graph[a].remove(Integer.valueOf(b));
            graph[b].remove(Integer.valueOf(a));


            System.out.println(graph[a]);
                
            boolean[] visited=new boolean[n+1];
            ArrayDeque<Integer> queue=new ArrayDeque<>();
            queue.add(a);
            int cnt1=1;
            visited[a]=true;
            
            while(!queue.isEmpty()){
                int curNode=queue.poll();
                for(int nextNode:graph[curNode]){
                    if(!visited[nextNode]){
                        cnt1++;
                        queue.add(nextNode);
                        visited[nextNode]=true;
                    }
                }
                
            }
            int cnt2=n-cnt1;
            answer=Math.min(answer,Math.abs(cnt1-cnt2));
            
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
            
            
            
        }
        
        
        
        return answer;
    }
}