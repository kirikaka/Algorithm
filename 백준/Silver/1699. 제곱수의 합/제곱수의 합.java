
import java.io.*;
import java.util.*;

public class Main {
    static int n,start;
    static int min=100001;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dp=new int[n+1];
        for(int i=1; i<=n; i++) {
            dp[i] = i;  // 최대 i개의 1^2
            for(int j=1; j*j<=i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j*j] + 1);
            }
        }

        System.out.println(dp(n));
    }

    static int dp(int n){
        if(dp[n]==0){
            dp[n]=min;
            for(int i=(int)Math.sqrt(n);i>=0;i--){
                int pow=(int)Math.pow(i,2);
                dp[n]=Math.min(dp(n-pow)+1,dp[n]);
            }
        }
        return dp[n];
    }
}
