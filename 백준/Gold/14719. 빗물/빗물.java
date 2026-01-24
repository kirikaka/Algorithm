import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H=Integer.parseInt(st.nextToken());
        int W=Integer.parseInt(st.nextToken());


        st=new StringTokenizer(br.readLine());
        int[] space=new int[W];

        for(int i=0;i<W;i++){
            int tmp=Integer.parseInt(st.nextToken());
            space[i]=tmp;
        }
        int rain=0;

        int leftHeight=space[0];
        int startIndex=0;
        for(int i=1;i<W;i++){
            int curHeight=space[i];
//            System.out.println("leftHeight="+leftHeight+" curHeight="+curHeight+" startIndex="+startIndex);
//            for(int c:space){
//                System.out.print(c+" ");
//            }
//            System.out.println();
            // 현재 높이가 이전 높이보다 클때
            if(curHeight>leftHeight){

                for(int j=startIndex;j<i;j++){
                    if(space[j]<curHeight ){

                        rain+=leftHeight-space[j];
                        space[j]=leftHeight;
                    }
                }
                startIndex=i;
                leftHeight=curHeight;


            }

            for(int j=startIndex;j<i;j++){
                if(space[j]<curHeight ){

                    rain+=curHeight-space[j];
                    space[j]=curHeight;
                }
            }
//            System.out.println("현재 빗물 높이 : "+ rain);
        }
        System.out.println(rain);

















    }
}
