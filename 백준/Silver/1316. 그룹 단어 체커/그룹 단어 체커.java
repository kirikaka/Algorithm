
import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static String[] words;
    static int count=0;
    static Set<Character> group;

    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());

        words=new String[n];
        for(int i=0;i<n;i++){
            words[i]=br.readLine();
        }
        for(int i=0;i<n;i++){
            check(words[i]);
        }

        System.out.println(count);

    }

    static void check(String word){
        char before='.';
        group=new HashSet<>();

        char[] letters=word.toCharArray();
        for(char c:letters){
            if(before=='.'){       // 첫 글자
                before=c;
                group.add(before);
                continue;
            }
            else if(before==c){    //연속된 글자
                continue;
            }
            else if(group.contains(c)){ //다른 글자지만 이미 진행했던 글자
                return;
            } else{                 // 새로운 글자
                group.add(c);
                before=c;

            }

        }
        count++;
    }
}
