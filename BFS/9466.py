from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
  n=int(input())
  student=[x for x in range(1,n+1)]
  togo=list(map(int,input().split()))

  visit=[False for _ in range(n)]
  
  """
  Cyclic 형태일 때는 팀을 이룰 수 있다. 
  두 명이라면 서로 선택해야 Cyclic 이므로 서로 선택해야 팀이라고 본다. 
  스스로 선택하면 하나의 팀이 될 수 있다.
  
  어느 팀에도 속하지 않는 학생의 수를 계산해라?
  
  togo를 순회하며 학생을 호출할 때마다 deque을 생성한다. deque에 넣는 것은 [호출자,지명자]
  해당 학생이 원하는 학생으로 호출하고 호출당한 학생이 또 다른 학생을 호출한다.
  호출해서 deque에 넣고 Cyclic인지 판단어케함?
  
  deque의 첫 원소의 [0]과 마지막 원소의 [1]이 같은지 비교?
  
  다르면 팀 없음 count +1
  
  
  - 순회로 접근했을 때만 visit True?
  - 방문했으면 visit에 True로 변경.
  - 이미 방문한 원소면 continue
  
  """
  count=0
  
  for i in range(n):
    que=deque()
    que.append([i+1,togo[i]])
    print("시작 QUE : ",que)
    visit[i]=True
    
    if i+1==togo[i]: #스스로 한팀이 되어버린 경우
      continue
    
    while True:
      
      if que[-1][1]==que[0][0]: #Cyclic 한 경우
        print("STOP 1")
        break
      
      call=que[-1][1]       # call : 마지막으로 넣은원소가 부르는 것.
      
      if call==togo[call-1]:          # togo[call-1] : 마지막으러 부른 원소가 뷰르는 것
        print("togo : ",togo[call-1])
        print("calll : ",call)
        print("STOP 2")
        break
      
      que.append([call,togo[call-1]]) #마지막에 들어간 번호, 해당 번호가 부르는 번호
      print(que)
    
    # while que:
      
    
    
    print(que)
    
  
  
  