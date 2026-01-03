import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static int[] nums;
    static int[] op=new int[4] ;
    static int min=Integer.MAX_VALUE;
    static int max=Integer.MIN_VALUE;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nums = new int[n];


        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) op[i] = Integer.parseInt(st.nextToken());

        backtracking(nums[0],1);
        System.out.println(max);
        System.out.println(min);

    }

    static void backtracking(int cur, int idx) {
        if(idx==n) {
            min=Math.min(min,cur);
            max=Math.max(max,cur);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (op[i] == 0) continue;

            op[i]--;
            int next;
            switch (i) {
                case 0: next = cur + nums[idx]; break;
                case 1: next = cur - nums[idx]; break;
                case 2: next = cur * nums[idx]; break;
                default: next = cur / nums[idx]; break; // 자바 정수 나눗셈
            }
            backtracking(next, idx + 1);
            op[i]++; // 복구
        }
    }



}
