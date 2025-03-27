import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        // 1. sides안에 있는 변보다 큰 변이 있을 때. 마지막 변이 sides 변을 합친 것보다 작아야함.
        // 2. sides 안에 가장 큰 변이 있을때. 
        // sum이 max보다 크고, 나머지 변이 max보다 작아야함.
        
        Arrays.sort(sides);
        int sum=sides[0]+sides[1];
        int max=sides[1];
        int min=sides[0];
        
        if (sum==3)  return 1;
        else return sum-max+min-1;
        
        
        // max-min<x<min+max
        
        
        
        // System.out.println(sides[1]);
    }
}