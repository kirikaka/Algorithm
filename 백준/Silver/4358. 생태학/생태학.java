
import java.util.*;
import java.io.*;

public class Main {
    static TreeMap<String,Double> dist=new TreeMap<>();
    static String input;
    static int cnt=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        while(true){
            input=br.readLine();

            if(input==null){
                break;
            }
            cnt++;
            if(dist.containsKey(input)){
                dist.replace(input,dist.get(input)+1.0);
            } else{
                dist.put(input,1.0);
            }

        }



        for(String s:dist.keySet()){
            double per= dist.get(s) / cnt *100;
            System.out.println(s +" "+String.format("%.4f",per));
        }


    }
}
