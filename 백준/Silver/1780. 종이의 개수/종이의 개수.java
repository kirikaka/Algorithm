
import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[][] paper;
    static int[] cnt = new int[3]; // 0: -1, 1: 0, 2: 1

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        paper = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solve(0, 0, N);

        System.out.println(cnt[0]); // -1
        System.out.println(cnt[1]); // 0
        System.out.println(cnt[2]); // 1
    }

    // (r, c)를 왼쪽 위로 하고, 크기가 size × size인 종이에 대해 처리
    static void solve(int r, int c, int size) {
        if (isSame(r, c, size)) {
            int value = paper[r][c];
            if (value == -1) cnt[0]++;
            else if (value == 0) cnt[1]++;
            else cnt[2]++;
            return;
        }

        int newSize = size / 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                solve(r + i * newSize, c + j * newSize, newSize);
            }
        }
    }

    static boolean isSame(int r, int c, int size) {
        int first = paper[r][c];
        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                if (paper[i][j] != first) return false;
            }
        }
        return true;
    }
}
