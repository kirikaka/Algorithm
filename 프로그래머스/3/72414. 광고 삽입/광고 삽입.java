class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        int play=strTosec(play_time);
        int adv=strTosec(adv_time);
        long[] dp=new long[play+1];
        
        for(String log:logs){
            String[] temp=log.split("-");
            int start=strTosec(temp[0]);
            int end=strTosec(temp[1]);
            dp[start]++;
            dp[end]--;
        }
        for(int i=1;i<dp.length;i++){
            dp[i]+=dp[i-1];
        }
        for(int i=1;i<dp.length;i++){
            dp[i]+=dp[i-1];
        }
        int startTime=0;
        long maxView=dp[adv-1];
        for(int i=0;i<play-adv+1;i++){
            if(maxView<dp[adv+i]-dp[i]){
                maxView=dp[adv+i]-dp[i];
                startTime=i+1;
            }
        }
        
        
        
        
        return secTostr(startTime);
    }
    
    int strTosec(String s){
        String[]temp=s.split(":");
        
        return Integer.parseInt(temp[0])*3600+Integer.parseInt(temp[1])*60+Integer.parseInt(temp[2]);
    }
    String secTostr(int s){
        int h=s/3600;
        int m=s%3600/60;
        int sec=s%60;
        
        return String.format("%02d:%02d:%02d",h,m,sec);
    }
}