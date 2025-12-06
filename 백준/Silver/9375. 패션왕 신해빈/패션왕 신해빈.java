
import java.util.*;
import java.io.*;

public class Main {
    static StringTokenizer st;
    static int T,n;
    static HashMap<String,Integer> cloth;


    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        st=new StringTokenizer(br.readLine());

        T=Integer.parseInt(st.nextToken());

        for(int i=0;i<T;i++) {
            st=new StringTokenizer(br.readLine());
            n=Integer.parseInt(st.nextToken());
            cloth=new HashMap<>();

            for(int j=0;j<n;j++) {
                st=new StringTokenizer(br.readLine());
                String a=st.nextToken();
                String type=st.nextToken();

                if(cloth.containsKey(type)) {
                    cloth.replace(type, cloth.get(type)+1);
                } else {
                    cloth.put(type,1);
                }

            }
            int answer=1;
            for(String key : cloth.keySet()) {
                answer=answer*( cloth.get(key)+1);
            }
            answer=answer-1;

            System.out.println(answer);
        }

    }
}
