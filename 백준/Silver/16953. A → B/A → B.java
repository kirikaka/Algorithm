
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


/* BFS로 접근해야 할 것 같아
* 하나의 수가 있으면 그 아래에 2를 곱한 것과 1을 오른쪽에 넣은 것을 두고
* depth를 기록하며 계속 내려가는 거지
* 그러다가 두 수가 모두 B보다 커져버리면 -1을 출력하면 되지 않을까?
* 해당 depth에 있는 모든 수가 B보다 커진 것을 어떻게 판별할까?
* 종료 조건 1 : Changing A ==B
* 종료 조건 2 : All of Changing A in depth > B -> -1
* * */

public class Main {
    static long A;
    static long B;
    static long count=0;
    static long[] cur;

    static boolean []visited;
    static Queue<long[]> queue;

    static void bfs(long start){
    /*
    * 1. QUE에 첫 시작을 넣는다.
    * 2. que가 모두 빌때까지 반복문?? 반복 끝나는건 start==B가 될때 인데,,,?
    * 3. 현재 숫자 cur을 꺼내온다.
    * 3-1. cur == B 면 멈추기.
    * 4. cur을 방문한 적 없으면 cur을 두배 한것과 1을 붙인것을 que에 넣는다.
    * 4-1. cur을 방문으로 만듬
    * 5.
    * */
        cur=new long[]{start,count};
        queue.offer(cur);

        while(!queue.isEmpty()){
            cur = queue.poll();


            if(cur[0]==B){
                count=cur[1];
                break;
            }
            if(!visited[(int)cur[0]]){
                if (cur[0]*2<=B){
                    queue.offer(new long[]{cur[0]*2, cur[1] + 1});
                }
                if(cur[0]*10+1<=B){
                    queue.offer(new long[]{cur[0]*10+1, cur[1] + 1});
                }
            }
            visited[(int)cur[0]]=true;


        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        visited = new boolean[(int)B+1];
        queue=new LinkedList<>();

        bfs(A);
        if(count==0){
            System.out.println(-1);
        } else{
            System.out.println(count+1);
        }

    }
}
