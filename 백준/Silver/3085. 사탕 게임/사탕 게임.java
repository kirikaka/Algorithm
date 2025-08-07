import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    static char[][]  board;
    static int n;
    static int max = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());

        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = s.charAt(j);
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                char temp1 = board[i][j];
                char temp2 = board[i][j + 1];

                board[i][j] = temp2;
                board[i][j + 1] = temp1;

                check();

                board[i][j] = temp1;
                board[i][j + 1] = temp2;
            }
        }

        for(int j=0;j<n;j++){
            for(int i=0;i<n-1;i++){
                char temp1 = board[i][j];
                char temp2 = board[i + 1][j];

                board[i][j] = temp2;
                board[i + 1][j] = temp1;

                check();

                board[i][j] = temp1;
                board[i + 1][j] = temp2;
            }
        }

        System.out.println(max);


    }
    static void check(){

        for(int  i=0;i<n;i++){
            int res1=1;
            for(int j=0;j<n-1;j++){
                if(board[i][j]==board[i][j+1]){
                    res1++;

                    max=Math.max(max,res1);
                } else{
                    res1=1;
                }
            }
        }

        for(int  i=0;i<n;i++){
            int res2=1;
            for(int j=0;j<n-1;j++){
                if(board[j][i]==board[j+1][i]){
                    res2++;
                    max=Math.max(max,res2);
                } else{
                    res2=1;
                }
            }
        }

    }
}
