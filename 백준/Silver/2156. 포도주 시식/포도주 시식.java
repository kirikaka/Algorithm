import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] wine=new int[n+2];
        for(int i=1;i<=n;i++){
            wine[i]=Integer.parseInt(br.readLine());
        }
        int[] dp =new int[n+2];
        int max=0;


        dp[1]=wine[1];
        dp[2]=wine[2]+wine[1];

        for(int i=3;i<=n;i++){
            dp[i]=Math.max(dp[i-3]+wine[i-1]+wine[i],Math.max(dp[i-2]+wine[i],dp[i-1]));
        }
        System.out.println(dp[n]);

        // 연속 3잔은 못먹는다
        // i번째 잔을 먹으려면
        // dp[i-2] + wine[i] 와 wine[i-1]+wine[i]+dp[i-3]
        // 첫잔 안먹을 수도 있으니까


    }
}
