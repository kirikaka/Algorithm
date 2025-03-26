

class Solution {
    public static int binary(String bin){
        int len=bin.length();
        int res=0;
        char b;
        for(int i=0;i<len;i++){
            b=bin.charAt(i);
            if(b=='1'){
                res+=Math.pow(2,len-i-1);
            }

        }
    
        return res;
    
    }
    public String solution(String bin1, String bin2) {
        String answer = "";
        
        int now=0;
        now+=binary(bin1)+binary(bin2);
        
        
        
        
        
        return Integer.toBinaryString(now);
    }
}

