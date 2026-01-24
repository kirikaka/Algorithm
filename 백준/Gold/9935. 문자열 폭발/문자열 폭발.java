import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String bomb = br.readLine();
        int m = bomb.length();
        char last = bomb.charAt(m - 1);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            sb.append(c);

            if (c == last && sb.length() >= m) {
                boolean ok = true;
                int start = sb.length() - m;
                for (int j = 0; j < m; j++) {
                    if (sb.charAt(start + j) != bomb.charAt(j)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) sb.delete(start, start + m);
            }
        }

        if (sb.length() == 0) System.out.print("FRULA");
        else System.out.print(sb);
    }
}
