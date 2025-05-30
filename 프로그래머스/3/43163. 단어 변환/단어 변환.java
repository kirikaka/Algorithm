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
    boolean onlyOneMatch(String word1,String word2){
        int count=0;
        for(int i=0;i<word1.length();i++){
            if(word1.charAt(i) != word2.charAt(i)){
                count++;
            }
        }
        if(count==1){
          return true;
        } 
        return false;
        
    }
    
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        HashSet<String>visit=new HashSet<>();
        
        visit.add(begin);
        ArrayDeque<Word>queue=new ArrayDeque<>();
        queue.add(new Word(begin, 0));
        while(!queue.isEmpty()){
            Word curWord=queue.poll();
            // System.out.println(curWord.word+" "+curWord.count);
            if(curWord.word.equals(target)){
                return curWord.count;
            }
            
            for(String nextWord:words){
                if(onlyOneMatch(curWord.word,nextWord) && !visit.contains(nextWord)){
                    queue.add(new Word(nextWord,curWord.count+1));
                    visit.add(nextWord);
                }
            }
        }
        
        
        
        return answer;
    }
}