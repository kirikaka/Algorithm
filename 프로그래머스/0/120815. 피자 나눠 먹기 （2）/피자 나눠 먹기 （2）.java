class Solution {
    public int solution(int n) {
        int answer = 0;

        if (n%2==0)
            n/=2;
        if (n%3==0)
            n/=3;
        return n;
        
    }
}