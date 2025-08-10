import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<List<Integer>> list =new ArrayList<>();
        int[] need=new int[N+1];

        for(int i=0;i<=N;i++){
            list.add(new ArrayList<>());
        }
        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.get(a).add(b);
            need[b]++;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=1;i<=N;i++){
            if(need[i]==0){pq.offer(i);}
        }
        StringBuilder sb = new StringBuilder();
        while(!pq.isEmpty()){
            int n = pq.poll();
            sb.append(n).append(" ");
            for(int next:list.get(n)){
                need[next]--;
                if(need[next]==0){
                    pq.offer(next);
                }
            }
        }
        System.out.println(sb.toString());


    }
}
