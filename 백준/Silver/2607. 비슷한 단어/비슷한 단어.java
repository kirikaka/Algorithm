import java.util.*;
import java.io.*;

public class Main {


    static int n;
    static String baseWord;
    static int[] words=new int[26];


    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());

        baseWord=br.readLine();
        for(int i=0;i<baseWord.length();i++){
            words[baseWord.charAt(i)-'A']++;
        }
        int ans=0;
        for(int i=1;i<n;i++){
            String s=br.readLine();
            if(check(s)) ans++;
        }

        System.out.println(ans);






    }


    static boolean check(String s){
        if(Math.abs(s.length()-baseWord.length())>1) return false;

        int[]cur=new int[26];
        for(int i=0;i<s.length();i++){
            cur[s.charAt(i)-'A']++;
        }
        int plus=0,minus=0;
        for(int i=0;i<26;i++){
            int diff=cur[i]-words[i];
            if(diff>0) plus+=diff;
            else minus+=-diff;
        }

        return (plus == 0 && minus == 0) ||
                (plus == 1 && minus == 0) ||
                (plus == 0 && minus == 1) ||
                (plus == 1 && minus == 1);
    }
}
