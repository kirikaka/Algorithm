import sys

n,m=map(int,sys.stdin.readline().split())
ans=[]

def back():
  if len(ans)==m: #base condition
    print(" ".join(map(str,ans))) #m개를 모두 선택했으면 출력하고
    return #현재 재귀 함수 종료한다. 
  for i in range(1,n+1): #재귀 함수
    if i not in ans: #i가 정답 리스트에없으면
      ans.append(i) # 리스트에 추가
      back() 
      ans.pop() #return을 하면 다시 여기로 돌아옴. 

back()