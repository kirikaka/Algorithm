import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static char[][] war;

    static int ourPower=0;
    static int urPower=0;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static Queue<int[]> que;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        war = new char[M][N];
        for(int i = 0; i < M; i++){
            char[]temp = br.readLine().toCharArray();
            for(int j = 0; j < N; j++){
                war[i][j] = temp[j];
            }
        }
//        for(int i = 0; i < N; i++){
//            for(int j = 0; j < M; j++){
//                System.out.print(war[i][j]);
//            }
//            System.out.println();
//        }
        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                if(war[i][j] == 'W'){
                    ourPower += bfs(i,j,'W');

                }else if(war[i][j] == 'B'){
                    urPower += bfs(i,j,'B');
                }

            }
        }


        System.out.println(ourPower + " " +  urPower);



    }
    static int bfs(int x, int y,char team){
        que = new LinkedList<>();
        int count=1;
        que.add(new int[]{x,y});
        war[x][y]='v';

        while(!que.isEmpty()){
            int []cur=que.poll();
            for(int i = 0; i < 4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if(nx>=0 && ny>=0 && nx<M && ny<N && war[nx][ny]==team){
                    que.add(new int[]{nx,ny});
                    count++;
                    war[nx][ny]='v';

                }
            }
        }
        return count*count;

    }
}
