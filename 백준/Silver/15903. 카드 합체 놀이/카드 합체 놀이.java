
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        PriorityQueue<Long> pq = new PriorityQueue<>();
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            pq.add(Long.parseLong(st.nextToken()));

        }
        for(int i = 0; i < M; i++){
            long num1=pq.poll();
            long num2=pq.poll();
            pq.add(num1+num2);
            pq.add(num1+num2);

//            System.out.println(pq);
        }
        long sum=0;
        for(int i = 0; i < N; i++){
            sum+=pq.poll();
        }
        System.out.println(sum);

    }
}
