import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main {

    public static void main(String[] args) throws Exception {
        // 1을 뺀다, 3으로 되면 3으로 나눈다. 2로 되면 2로 나눈다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());

        int[]dp=new int[n+1];
        int[]trace=new int[n+1];

        dp[0]=dp[1]=0;

        for(int i=2;i<=n;i++){
            dp[i]=dp[i-1]+1;
            trace[i]=i-1;
            if(i%3==0 && dp[i]>dp[i/3]+1){
                dp[i]=dp[i/3]+1;
                trace[i]=i/3;
            }
            if(i%2==0 && dp[i]>dp[i/2]+1){
                dp[i]=dp[i/2]+1;
                trace[i]=i/2;
            }
        }

        System.out.println(dp[n]);
        StringBuilder sb=new StringBuilder();
        for(int i=n;i>0;i=trace[i]){
            sb.append(i+" ");
        }
        System.out.println(sb);
    }

}
