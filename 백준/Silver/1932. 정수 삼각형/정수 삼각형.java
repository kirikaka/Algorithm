import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[][] dp;
    static int[][] og;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        og = new int[n][n];
        dp = new int[n][n];


        for(int i=0;i<n;i++){
            String[] s=br.readLine().split(" ");
            for(int j=0;j<=i;j++){
                og[i][j] = Integer.parseInt(s[j]);

            }

        }
        //맨 왼,중간, 맨오 나눠서 생각하기
        dp[0][0]=og[0][0];
        for(int i=1;i<n;i++){
            // 맨 왼
            dp[i][0]=dp[i-1][0]+og[i][0];
            for(int j=1;j<i;j++){
                dp[i][j]=Math.max(dp[i-1][j]+og[i][j],dp[i-1][j-1]+og[i][j]);
            }

            // 맨 오
            dp[i][i]=dp[i-1][i-1]+og[i][i];

        }

        int max=0;
        for(int i=0;i<n;i++){
            max=Math.max(max,dp[n-1][i]);
        }
        System.out.println(max);

    }
}
