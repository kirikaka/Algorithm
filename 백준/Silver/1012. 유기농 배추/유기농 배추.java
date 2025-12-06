
import java.util.*;
import java.io.*;

public class Main {
    static int T,M,N,K,x,y;
    static StringTokenizer st;
    static int[][] baechu;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st= new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        for(int u=0;u<T;u++){
            answer=0;

            st= new StringTokenizer(br.readLine());

            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            baechu=new int[N][M];
            visited=new boolean[N][M];

            for(int i=1;i<=K;i++) {
                st= new StringTokenizer(br.readLine());
                x=Integer.parseInt(st.nextToken());
                y=Integer.parseInt(st.nextToken());

                baechu[y][x]=1;
            }


            for(int i=0;i<N;i++) {
                for(int j=0;j<M;j++) {
                    if(baechu[i][j]==1 && !visited[i][j]) {
                        bfs(i,j);
                        answer++;
                    }

                }

            }
            System.out.println(answer);


        }

    }

    static void bfs(int i, int j) {
        visited[i][j]=true;
        Queue<int[]> q=new LinkedList<>();
        q.add(new int[]{i,j});

        while(!q.isEmpty()) {
            int[] a=q.poll();
            for(int k=0;k<4;k++) {
                int nextY=a[0]+dy[k];
                int nextX=a[1]+dx[k];

                if(nextX>=0 && nextX<M && nextY>=0 && nextY<N) {
                    if(!visited[nextY][nextX] && baechu[nextY][nextX]==1) {
                        visited[nextY][nextX]=true;
                        q.add(new int[]{nextY,nextX});
                    }
                }


            }
        }
    }
}
