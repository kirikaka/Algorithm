import java.util.*;


class Solution {
    class Word{
        int count;
        String word;
        Word(String word,int count){
            this.count=count;
            this.word=word;
        }
    }
    public boolean onlyOneMatch(String word1,String word2){
        int count =0;
        for(int i=0;i<word1.length();i++){
            if(word1.charAt(i)==word2.charAt(i)){
                count++;
            }
        }
        if(word1.length()-count==1){
            return true;
        }        
        return false;
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        // 단어의 방문 여부를 따지고. 두 단어마다 차이나는 알파벳 개수가 1개일때 이동하도록. 
        // BFS로 방문하면 항상 최소이다. 
        HashSet<String> visitWord= new HashSet<>();
        ArrayDeque<Word> queue=new ArrayDeque<>(); 
        visitWord.add(begin);
        queue.offer(new Word(begin,0));
        
        while(!queue.isEmpty()){
            Word current=queue.poll();
            
            String curWord=current.word;
            int curCount=current.count;
            
            
            if(curWord.equals(target)){
                return curCount;
            }
            
            for(String nextWord:words){
                if(!visitWord.contains(nextWord) && onlyOneMatch(curWord,nextWord)){
                    queue.offer(new Word(nextWord,curCount+1));
                    visitWord.add(nextWord);
                }
            }
            
            
            
        }
        
        
        
        
        return answer;
    }
}