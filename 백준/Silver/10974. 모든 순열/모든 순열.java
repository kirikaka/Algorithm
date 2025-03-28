import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;



/*
재귀 함수로 설계  -> 사전 순 아니라 실패.
현재 위치가 배열의 마지막 인덱스에 도달하면 순열 출력 후 재귀 종료
현재 위치부터 배열 끝까지 순회하며 순열 생성

현재 위치 요소와 다음 요소 교환 -> 첫 요소 교환
다음 위치에서 재귀 호출 -> 하위 순열 생성 시작
다시 원래 상태로 되돌리기 -> 탐색을 다했으면 복구
첫 요소(arr[0])를 바꿔서 해봤으니 다음은 두번째 요소(arr[1]) 로 이동해서 확인.
swap을 사용하는 방법은 사전순 출력을 보장 하지않음


public class BJ10974 {
    public static void permutation(int[] arr, int start){
        if(start==arr.length-1){  //시작요소가 배열의 끝에 도착했으면 모두 확인한것
            printArray(arr);
            return ;
        }
        for(int i=start; i<arr.length; i++){
            swap(arr,start,i);
            permutation(arr,start+1);
            swap(arr,start,i);
        }
    }

    public static void swap(int[] arr,int start,int i){
        int temp = arr[start];
        arr[start] = arr[i];
        arr[i] = temp;
    }

    public static void printArray(int[] arr){

        for(int num:arr){
            System.out.printf("%d ",num);
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int n=Integer.parseInt(st.nextToken());

        int[] arr=new int[n];
        for(int i=1;i<=n;i++){
            arr[i-1]=i;
        }
        permutation(arr,0);
    }
}

*/
/*
사전순으로 정렬하는 방법.
visited 배열을 써서 하라는데?



 */



public class Main {
    static int n;
    static int[] arr;
    static boolean[] visited;
    static StringBuilder sb=new StringBuilder();

    public static void perm(int depth,int []current){
        if (depth==n){
            for(int num:current){
                sb.append(num).append(" ");
            }
            sb.append('\n');
            return;
        }

        for(int i=0;i<current.length;i++){
            if(!visited[i]){
                visited[i]=true;
                current[depth]=arr[i];
                perm(depth+1,current);
                visited[i]=false;
            }
        }
    }



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        arr=new int[n];
        visited=new boolean[n];

        for(int i=1;i<=n;i++){
            arr[i-1]=i;
        }
        perm(0,new int[n]);
        System.out.println(sb.toString());


    }
}
