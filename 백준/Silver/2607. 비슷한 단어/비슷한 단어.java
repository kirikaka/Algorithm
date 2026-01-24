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
        // 단어 길이차이가 1보다 크면 당연히 실패
        if(Math.abs(s.length()-baseWord.length())>1) return false;

        //현재 단어 구성 확인
        int[]cur=new int[26];
        for(int i=0;i<s.length();i++){
            cur[s.charAt(i)-'A']++;
        }
        int plus=0,minus=0;
        // 첫단어랑 비교단어를 차를 계산함 
        // 첫단어에 없으면 minus에, 비교단어에 없으면 plus에 차이 만큼 더함
        for(int i=0;i<26;i++){
            int diff=cur[i]-words[i];
            if(diff>0) plus+=diff;
            else minus+=-diff;
        }
        //plus, minus가 아래와 같지 않으면 (=구성이 너무 다르면) false
        return (plus == 0 && minus == 0) ||
                (plus == 1 && minus == 0) ||
                (plus == 0 && minus == 1) ||
                (plus == 1 && minus == 1);
    }
}
