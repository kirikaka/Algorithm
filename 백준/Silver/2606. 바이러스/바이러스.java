
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static boolean[] visited;
    static ArrayList<Integer>[] graph;
    static int count=0;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        visited=new boolean[N+1];
        graph=new ArrayList[N+1];
        for(int i=0;i<N+1;i++){
            graph[i]=new ArrayList<>();
        }
        // 연결리스트 입력받기
        for(int i=0;i<M;i++){
            int x=sc.nextInt();
            int y=sc.nextInt();

            graph[x].add(y);
            graph[y].add(x);
        }

        dfs(1);

        System.out.println(count);


    }
    static void dfs(int v){
        visited[v]=true;

        for(int w:graph[v]){
            if(!visited[w]){
                count++;
                dfs(w);
            }
        }
    }

}
