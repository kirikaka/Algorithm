import java.util.*;
import java.io.*;



public class Main {
    static int n;   // 기둥의 개수
    static int L,H; // 기둥 위치, 높이

    static int answer=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[][] pillar = new int[n][2];
        StringTokenizer st;
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            pillar[i][0] = Integer.parseInt(st.nextToken());
            pillar[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(pillar,(a,b)->a[0]-b[0]);


        int maxHeight=0;
        int maxIdx=0;
        for(int i=0;i<n;i++){
            if(pillar[i][1]>maxHeight){
                maxHeight=pillar[i][1];
                maxIdx=i;
            }
        }

        int startMax=-1, endMax=-1;
        for(int i=0;i<n;i++){
            if(pillar[i][1]==maxHeight){
                if(startMax==-1) startMax=i;
                endMax=i;

            }
        }


        // 최대 높이 이전 구하기.
        int beforeHeight=pillar[0][1];
        int beforeIdx=0;
        int before=0;
        for(int i=0;i<=maxIdx;i++){
            if(pillar[i][1]>beforeHeight){
                int tmp=beforeHeight*(pillar[i][0]-pillar[beforeIdx][0]);
                before+=tmp;
                beforeIdx=i;
                beforeHeight=pillar[i][1];
            }
        }
        before += beforeHeight * (pillar[startMax][0] - pillar[beforeIdx][0]);

//        System.out.println(before);




        // 최대 높이 이후 구하기.

        int afterHeight=pillar[n-1][1];
        int afterIdx=n-1;

        int after=0;
        for(int i=n-1;i>=maxIdx;i--){
            if(pillar[i][1]>afterHeight){
                int tmp=afterHeight*(pillar[i][0]-pillar[afterIdx][0]);
                if(tmp<0) tmp*=(-1);

                after+=tmp;
                afterIdx=i;
                afterHeight=pillar[i][1];
            }
        }

        after += afterHeight * (pillar[afterIdx][0] - pillar[endMax][0]);




        answer+=before+after+maxHeight*(pillar[endMax][0]-pillar[startMax][0]+1);

        System.out.println(answer);










    }

}
