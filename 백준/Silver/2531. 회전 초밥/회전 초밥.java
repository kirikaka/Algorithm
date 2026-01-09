import java.util.*;
import java.io.*;

public class Main {
    static int N,d,k,c;
    static int[]sushi;

    static Set<Integer>plate;
    static int answer=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        sushi = new int[N];
        for(int i=0;i<N;i++){
            sushi[i]=Integer.parseInt(br.readLine());
        }

        int[] cnt=new int[d+1];
        // 컨베이어 벨트 위에는 중복이 있을 수 있지만 중복해서 먹지 않으려 한다.
        // 다양하게 먹으려고함
        // k개만큼 담으면 c번호를 무료로 먹을 수 있다.
        // 가장 다양한 초밥을 먹을 수 있는 경우를 찾아라.
        int kind=0;
        for(int i=0;i<k;i++){
            int s=sushi[i];
            if(cnt[s]==0){
                kind++;
            }
            cnt[s]++;
        }
        answer=kind+(cnt[c]==0?1:0);

        for(int i=1;i<N;i++){
            int out=sushi[i-1];
            cnt[out]--;
            if(cnt[out]==0){
                kind--;
            }
            int in=sushi[(i+k-1)%N];
            if(cnt[in]==0){
                kind++;
            }
            cnt[in]++;

            int cur=kind+(cnt[c]==0?1:0);
            answer=Math.max(answer,cur);

        }

        System.out.println(answer);



    }



}
