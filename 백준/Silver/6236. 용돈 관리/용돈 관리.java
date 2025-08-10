import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] money = new int[N];
        int max = 0;
        long sum = 0;

        for (int i = 0; i < N; i++) {
            money[i] = Integer.parseInt(br.readLine());
            if (money[i] > max) max = money[i];
            sum += money[i];
        }

        long start = max;
        long end = sum;
        long answer = 0;

        while (start <= end) {
            long mid = (start + end) / 2;

            // 인출 횟수 계산
            int count = 1;  // 인출 횟수
            long total = mid;

            for (int i = 0; i < N; i++) {
                if (money[i] > total) {
                    count++;
                    total = mid;
                }
                total -= money[i];
            }

            if (count > M) {
                start = mid + 1;  // 인출 횟수가 많으므로 인출 금액 늘리기
            } else {
                answer = mid;     // 인출 횟수 적거나 같으면 금액 줄여도 됨
                end = mid - 1;
            }
        }

        System.out.println(answer);
    }
}