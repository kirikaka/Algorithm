
import java.util.*;
import java.io.*;
public class Main {
    static int[] muscle;
    static boolean[] check;
    static int N;
    static int K;
    static int cnt = 0;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); // 운동 키트 개수
        K = Integer.parseInt(st.nextToken()); //만큼 매일 줄어듦
        muscle = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            muscle[i] = Integer.parseInt(st.nextToken());
        }
        check = new boolean[N];
        int muscleCnt = 500;
        int depth = 1;
        backTracking(muscleCnt, depth);
        System.out.println(cnt);
    }

    static void backTracking(int muscleCnt, int depth) {
        if (muscleCnt < 500) {
            return;
        }
        if(depth==N) {
            cnt++;
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!check[i]) {
                check[i] = true;
                backTracking(muscleCnt + muscle[i]-K, depth+1);
                check[i] = false;
            }
        }
    }
}
