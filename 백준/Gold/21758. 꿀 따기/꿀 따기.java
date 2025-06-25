
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // 최대한 많은 양봉을 가지게 시작해야한다.
    // 모든 경우의 수를 계산해야한다.
    // 벌통이 왼 오 중 으로 나눠서 하기
    //
    static long answer=0;
    static int[] honey;
    static int honeyPot;
    static int bee1;
    static int bee2;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());

        honey=new int[n];
        String[] honeyStr=br.readLine().split(" ");
        for(int i=0;i<n;i++){
            honey[i]=Integer.parseInt(honeyStr[i]);
        }
        left();
        right();
        center();

        System.out.println(answer);




    }
    // 벌통 왼쪽에 있으면
    // 벌1 은 가장 오른쪽에 있고
    // 벌2는 오른쪽 하나전부터 옮겨가면서 최댓값확인
    static void left(){
//        System.out.println("LEFT Strat");
        honeyPot=0;
        bee1=n-1;
        bee2=bee1-1;

        long sum=0;
        for(int i=bee2;i>honeyPot;i--){
            long temp1=0;
            for(int j=honeyPot;j<bee1;j++){
                if(j==i){

                    continue;
                }
                temp1+=honey[j];
            }
//            System.out.println("temp1 = " + temp1);

            long temp2=0;
            for(int j=honeyPot;j<i;j++){
                temp2+=honey[j];
            }
//            System.out.println("temp2 = " + temp2);

            sum=Math.max(sum,temp1+temp2);
//            System.out.println("sum = " + sum+"  현재 bee2는 : "+i);


        }
        answer=Math.max(answer,sum);




    }


    static void right(){
//        System.out.println("RIGHT Strat");

        honeyPot=n-1;
        bee1=0;
        bee2=bee1+1;

        long sum=0;
        for(int i=bee2;i<honeyPot;i++){
            long temp1=0;
            for(int j=honeyPot;j>bee1;j--){
                if(j==i){

                    continue;
                }
                temp1+=honey[j];
            }
//            System.out.println("temp1 = " + temp1);

            long temp2=0;
            for(int j=honeyPot;j>i;j--){
                temp2+=honey[j];
            }
//            System.out.println("temp2 = " + temp2);

            sum=Math.max(sum,temp1+temp2);
//            System.out.println("sum = " + sum+"  현재 bee2는 : "+i);


        }
        answer=Math.max(answer,sum);
    }

    // 벌1,2가 가장 끝에 위치하고
    // 벌통 옮겨가면서 최댓값 측정.
    static void center(){
//        System.out.println("CENTER Strat");

        bee1=0;
        bee2=n-1;
        honeyPot=1;
        long sum=0;


        for(int j=honeyPot;j<bee2;j++){
            long temp1=0;
            for(int i=j;i>bee1;i--){

                temp1+=honey[i];
            }
//            System.out.println("temp1 = " + temp1);
            long temp2=0;
            for(int i=j;i<bee2;i++){

                temp2+=honey[i];
            }

//            System.out.println("temp2 = " + temp2);

            sum=Math.max(sum,temp1+temp2);
        }
        answer=Math.max(answer,sum);


    }


}
