class Solution {
    public String solution(String new_id) {
        String  a=new_id;

        // 1
        a = a.toLowerCase();
        System.out.println("1 a = " + a);

        // 2
        a = a.replaceAll("[^a-z0-9-_.]", "");
        System.out.println("2 a = " + a);

        // 3
        a = a.replaceAll("[.]{2,}", ".");
        System.out.println("3 a = " + a);

        // 4
        a = a.replaceAll("^[.]", "");
        a = a.replaceAll("[.]$", "");
        System.out.println("4 a = " + a);

        // 5
        if (a.length() == 0) a = "a";
        System.out.println("5 a = " + a);

        // 6
        if (a.length() >= 16) a = a.substring(0, 15);
        a = a.replaceAll("[.]$", "");
        System.out.println("6 a = " + a);

//        a = "de";
        // 7단계
        if(a.length() <= 2) {
            while(a.length()<3) {
                char word = a.charAt(a.length() - 1);
                a+=word;
            }

//            System.out.println(word);
        }
        System.out.println("7 a = " + a);

    
        return a;
    }
}