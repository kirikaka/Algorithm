import java.io.*;
import java.util.*;

public class Main {
    static int N,K;
    static boolean[] visited;
    static Queue<int[]> que;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());
        visited=new boolean[100001];

        int ans=bfs(N,K);

        System.out.println(ans);


    }
    static int bfs(int start,int target) {
        if(start==target){
            return 0;
        }


        que=new LinkedList<>();
        que.add(new int[]{start,0});
        visited[start]=true;
        while(!que.isEmpty()){
            int[] cur=que.poll();
            if(cur[0]==target){
                return cur[1];
            }
            int next=0;
            for(int i=0;i<3;i++){
                if(i==0) next=cur[0]*2;
                else if(i==1) next=cur[0]-1;
                else if(i==2) next=cur[0]+1;

                if(next<0 || next>100000 || visited[next] ) continue;

                que.add(new int[]{next,cur[1]+1});
                visited[next]=true;
            }



        }
        return -1;
    }


}
