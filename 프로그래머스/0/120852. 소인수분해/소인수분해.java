import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> ans = new ArrayList<Integer>();
        int num=n;
        for(int i=2;i<=n;i++){
            if(num%i==0){
                while(num % i == 0){
                    ans.add(i);
                    num=num/i;                    
                }

            }
        }
        Set<Integer> set = new HashSet<>(ans);
        
        int[] answer=set.stream().mapToInt(i->i).toArray();
        Arrays.sort(answer);
        
        
        
        return answer;
    }
}