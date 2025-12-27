import java.util.*;
import java.io.*;

public class Main {
    static int N,currentTime;
    static int[] time;
    static int[] pay;
    static int[] dp;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());
        time=new int[N+2];
        pay=new int[N+2];


        for(int i=1;i<=N;i++)  {
            st=new StringTokenizer(br.readLine());
            time[i]=Integer.parseInt(st.nextToken());
            pay[i]=Integer.parseInt(st.nextToken());
        }

        dp=new int[N+2];
        for(int i=N;i>=1;i--)  {
            int next=i+time[i];
            if(next<=N+1){
                dp[i]=Math.max(dp[i+1],dp[next]+pay[i]);
            } else{
                dp[i]=dp[i+1];
            }
        }

        System.out.println(dp[1]);

    }
}
