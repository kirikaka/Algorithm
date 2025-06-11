
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int INF = 987654321;
    static int N;
    static int M;
    static int[][] dist;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());
        M=Integer.parseInt(br.readLine());
        dist=new int[N+1][N+1];
        StringTokenizer st;

        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                if(i==j){
                    dist[i][j]=0;
                    continue;
                }
                dist[i][j]=INF;

            }
        }


        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int c=Integer.parseInt(st.nextToken());

            dist[a][b]=Math.min(dist[a][b], c);
        }

        for(int k=1;k<=N;k++){
            for(int i=1;i<=N;i++){
                for(int j=1;j<=N;j++){

                    dist[i][j]=Math.min(dist[i][j],dist[i][k]+dist[k][j]);
                }
            }
        }
        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                if(dist[i][j]==INF){
                    System.out.print(0+" ");
                }else{
                    System.out.print(dist[i][j]+" ");
                }

            }
            System.out.println();
        }




    }

}
