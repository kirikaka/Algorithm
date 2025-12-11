
import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        char[] names=br.readLine().toCharArray();
        Arrays.sort(names);

        HashMap<Character,Integer> map=new HashMap<>();
        for(char c:names) {
            if(!map.containsKey(c)) {
                map.put(c,1);
            }else{
                map.replace(c,map.get(c)+1);

            }

        }
        StringBuilder ans= new StringBuilder();


        int count=0;
        char cent = 0;
        for(char c:map.keySet()) {
            if(map.get(c)%2!=0) {
                cent=c;
                count++;
            }
            for(int i=0;i<(map.get(c)/2);i++){
                ans.append(c);
            }
        }
        char[] sorted_ans=ans.toString().toCharArray();
        Arrays.sort(sorted_ans);
        StringBuilder ans2= new StringBuilder(new String(sorted_ans));



        if(count>1) {
            System.out.println("I'm Sorry Hansoo");
        } else{


            System.out.print(ans2);
            if(cent!=0){
                System.out.print(cent);
            }
            System.out.println(ans2.reverse());

        }






    }
}
