import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int N;
    static char[] bulbs, target;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        bulbs = br.readLine().toCharArray();
        target = br.readLine().toCharArray();
        
        // 첫번째 스위치를 누르지 않는 경우
        char[] bulbsCopy1 = Arrays.copyOf(bulbs, N);
        int count1 = switchBulbs(bulbsCopy1, false);
        
        // 첫번째 스위치를 누르는 경우
        char[] bulbsCopy2 = Arrays.copyOf(bulbs, N);
        int count2 = switchBulbs(bulbsCopy2, true);
        
        if (count1 == -1 && count2 == -1) {
            System.out.println(-1);
        } else if (count1 == -1) {
            System.out.println(count2);
        } else if (count2 == -1) {
            System.out.println(count1);
        } else {
            System.out.println(Math.min(count1, count2));
        }
    }
    
    static int switchBulbs(char[] arr, boolean pressFirst) {
        int count = 0;
        if (pressFirst) {
            toggle(arr, 0);
            toggle(arr, 1);
            count++;
        }
        
        for (int i = 1; i < N; i++) {
            if (arr[i-1] != target[i-1]) {
                // i번째 스위치를 눌러서 i-1, i, i+1 번째 전구 상태 변경
                toggle(arr, i-1);
                toggle(arr, i);
                if (i+1 < N) toggle(arr, i+1);
                count++;
            }
        }
        
        if (Arrays.equals(arr, target)) {
            return count;
        } else {
            return -1;
        }
    }
    
    static void toggle(char[] arr, int idx) {
        arr[idx] = (arr[idx] == '0') ? '1' : '0';
    }
}
