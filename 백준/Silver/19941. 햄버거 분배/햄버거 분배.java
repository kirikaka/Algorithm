
import java.util.*;
import java.io.*;

public class Main {
    static int n,k,answer;
    static char[] table;
    static boolean[] visited;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException{
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        st=new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());

        String input=br.readLine();
        table=input.toCharArray();

        visited=new boolean[n];

        for(int i=0;i<n;i++){
            if(table[i]=='P'){
                visited[i]=true;
                check(i);
            }

        }

        System.out.println(answer);

    }
    static void check(int i){
        int start=0;
        if(i-k>=0){
            start=i-k;
        }
        int end=n;
        if(i+k+1<=n){
            end=i+k+1;
        }
        for(int j=start;j<end;j++){
            if(table[j]=='H'&& !visited[j]){

                visited[j]=true;
                answer++;
                break;
            }
        }
    }

}
