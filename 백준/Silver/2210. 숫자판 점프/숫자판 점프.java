import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    static String[][] num=new String[5][5];
    static HashSet<String> answer = new HashSet<>();

    static int dx[] = {0, 0, 1, -1}; // 상하좌우 이동
    static int dy[] = {1, -1, 0, 0}; // 상하좌우 이동
    public static void dfs(int x,int y,String route,int count){
        if(count==5){
            answer.add(route);
            return;
        }
        for(int i=0;i<4;i++){
            int nowX=dx[i]+x;
            int nowY=dy[i]+y;
            if(0<=nowX &&nowX<5 && 0<=nowY && nowY<5){
                dfs(nowX,nowY,route+num[nowX][nowY],count+1);
            }
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        int dx[] = {0, 0, 1, -1}; // 상하좌우 이동
        int dy[] = {1, -1, 0, 0}; // 상하좌우 이동



        for(int i=0;i<5;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<5;j++){
                num[i][j]=st.nextToken();

            }
        }

        for(int i=0;i<5;i++){
            for(int j=0;j<5;j++){
                dfs(i,j,num[i][j],0);
            }
        }


        /*
            6자리수를 서로 다른 2수로 채우면 15 6C2아니냐? 그러면 서로 다른 수의 개수를 세보자?  -> 실패
            dfs로 탐색하고

        */
        System.out.println(answer.size());

    }
}
