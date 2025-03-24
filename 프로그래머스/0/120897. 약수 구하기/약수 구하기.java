import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=1;i<n+1;i++){
            if (n%i==0){
                ans.add(i);
            }
        }
        int[] answer=ans.stream().mapToInt(Integer::intValue).toArray();
        
        
        return answer;
    }
}