import java.util.*;
import java.lang.*;
import java.io.*;


public class Main {
    static int n,pair;
    static ArrayList<ArrayList<Integer>> graph;
    static boolean[] visited;
    static int count=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        pair = Integer.parseInt(br.readLine());
        graph = new ArrayList<>();
        visited = new boolean[n+1];

        for(int i=0;i<=n;i++)
            graph.add(new ArrayList<>());

        StringTokenizer st;
        for(int i = 0; i < pair; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        bfs(1);
        System.out.println(count);


    }
    static void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        visited[start] = true;
        q.add(start);
        while(!q.isEmpty()){
            int cur = q.poll();
            for(int i : graph.get(cur)){
                if(!visited[i]){
                    visited[i] = true;
                    q.add(i);
                    count++;
                }
            }
        }

    }
}
