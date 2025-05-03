import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String[] a = input.split("-");

        int[] res = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            String[] b = a[i].split("\\+");
            int res_b = 0;
            for (String k : b) {
                res_b += Integer.parseInt(k);
            }
            res[i] = res_b;
        }

        int result = res[0];
        for (int i = 1; i < res.length; i++) {
            result -= res[i];
        }

        System.out.println(result);
        sc.close();
    }
}