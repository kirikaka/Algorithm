
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/* DP 조건
* 1. 겹치는 소문제 : 문제를 작게 나누고 결과를 재사용해서 원하는 결과 도출
* 2. 최적 부분 구조 : 소문제 최적 결과로 전체 문제의 최적 결과를 낼수 있는가?
* 소문제의 결과를 저장하고 결과값 도출 조건을 구해둔다.
* */


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] box=new int[n];
        int[] dp=new int[n];
        for(int i=0;i<n;i++){
            box[i]=Integer.parseInt(st.nextToken());
        }
        // 0. 기저 사례
        dp[0]=1;
        // 1. 이전 박스가 나보다 작다면 이전 박스가 넣을 수 있는 박스+1
        // 2. DP와 LIS 알고리즘(Longest Increasing Subsequence)를 활용
        // 3. 
        int max=dp[0];
        for(int i=0;i<n;i++){
            dp[i]=1;
            for(int j=0;j<i;j++){
                if(box[i]>box[j]){
                    dp[i]=Math.max(dp[i],dp[j]+1);
                }
            }
            max=Math.max(max,dp[i]);
        }

        System.out.println(max);


    }

}
