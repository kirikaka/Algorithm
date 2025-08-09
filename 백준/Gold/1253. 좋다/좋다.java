import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] arr = new long[N];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        
        Arrays.sort(arr);
        
        int goodCount = 0;
        
        // 각 수에 대해 투포인터로 확인
        for (int i = 0; i < N; i++) {
            long target = arr[i];
            int start = 0;
            int end = N - 1;

            while (start < end) {
                if (start == i) {  // 자신 인덱스는 패스
                    start++;
                    continue;
                }
                if (end == i) {    // 자신 인덱스는 패스
                    end--;
                    continue;
                }
                
                long sum = arr[start] + arr[end];
                if (sum == target) {
                    goodCount++;
                    break;
                } else if (sum < target) {
                    start++;
                } else {
                    end--;
                }
            }
        }
        
        System.out.println(goodCount);
    }
}
