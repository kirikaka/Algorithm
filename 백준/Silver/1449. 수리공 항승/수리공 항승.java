
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N,L;
    static int [] cracks;
    static int ans=1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        cracks = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cracks[i] = Integer.parseInt(st.nextToken());

        }
        Arrays.sort(cracks);


        int left=L;

        for(int i=1;i< cracks.length;i++) {
            int dif=cracks[i]-cracks[i-1];
            if(dif<left){
                left-=dif;
            } else {
                ans++;
                left=L;
            }

        }
        System.out.println(ans);

    }
}
