import java.util.*;

class Solution {
    class Word{
        String word;
        int count;
        
        Word(String word,int count){
            this.word=word;
            this.count=count;
        }
    }
    int getDifferentCount(String word1,String word2){
        int count=0;
        for(int i=0;i<word1.length();i++){
            if(word1.charAt(i) != word2.charAt(i) ){
                count++;
            }
        }
        return count;
        
    }
    
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        HashSet<String> visited=new HashSet<>();
        Queue<Word> queue=new ArrayDeque<>();
        queue.offer(new Word(begin,0));
        visited.add(begin);
        String last;
        
        while(!queue.isEmpty()){
            
            Word current=queue.poll();
            
            System.out.println(current.word+" "+current.count);
            if (current.word.equals(target)){
                return current.count;
            }
            for(String nextWord:words){
                if(getDifferentCount(current.word,nextWord)==1){
                    if(!visited.contains(nextWord)){
                        queue.offer(new Word(nextWord,current.count+1));
                        visited.add(nextWord);
                    }
                }
            }
            
            
        }
        
        
        return answer;
    }
}