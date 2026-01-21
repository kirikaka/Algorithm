import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        TreeSet<Integer> treeSet = new TreeSet<>();


        // 걍 소수를 미리 구해놓자.
        int[] sosu=new int[1000001];

        for(int i=2;i<=i*i;i++){
            if(sosu[i]!=-1 && i%2==1) {
                treeSet.add(i);

            }

            for(int j=2*i;j<1000001;j+=i){   //자기 자신이 아니므로 j는 2*i에서부터 시작.
                sosu[j]=-1;
            }
        }




        while(true){
            int n=Integer.parseInt(br.readLine());

            if(n==0) break;
            boolean flag=false;
            for(int i=3;i<n;i++){
                if(sosu[i]!=-1 && sosu[n-i]!=-1) {
                    bw.write(n+" = "+i+" + "+(n-i)+"\n");
                    flag=true;
                    break;
                }

            }
            if(!flag) {
                bw.write("Goldbach's conjecture is wrong"+"\n");
            };





        }
        bw.flush();
        bw.close();
    }

    // 원래 따로 빼서 반복문안에서 돌렸는데, 이렇게 하니까 시간초과가 나옴.
    static int[] func(int n){
        int[]ans=new int[2];
        // 에라토스테네스의 체 공부하기
        // 2부터 시작해서. 자기 자신이 아닌 배수를 지우기.

        int[] sosu=new int[1000001];
        for(int i=2;i<=n;i++){
            if(sosu[i]!=-1) continue;

            for(int j=2*i;j<=n;j+=i){   //자기 자신이 아니므로 j는 2*i에서부터 시작.
                sosu[j]=-1;
            }
        }
        TreeSet<Integer> deq=new TreeSet<>();

        for(int i=2;i<=n;i++){
            if(sosu[i]!=-1 && i%2==1){
                deq.add(i);
            }
        }
        int min=0;

        for(int a:deq){
            if(deq.contains(n-a) && n-a-a>=min){
                min=n-a-a;
                ans[0]=a;
                ans[1]=n-a;
            };
        }









        return ans;
    }
}















