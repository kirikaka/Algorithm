from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
  n=int(input())
  # student=[x for x in range(1,n+1)]
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
  
  다르면 팀 없음 count + 1
  
  
  - 순회로 접근했을 때만 visit True?
  - 방문했으면 visit에 True로 변경.
  - Cycle이 나온 경우 바로 break하고
  - 
  - 이미 방문한 원소면 continue
  
  """
  count=0
  
  for i in range(n):
    if i+1==togo[i]: #스스로 한팀이 되어버린 경우
      visit[i]=True
      count+=1
      continue
    
    if visit[i]:    #이미 방문한 경우
      continue
        
    que=deque()
    que.append([i+1,togo[i]])
    print("시작 QUE : ",que)
    visit[i]=True
    
    while True:
      # print("현재 : ",que)
      last=que[-1][1]
      
      if que[-1][1]==que[0][0]:     #  완벽히 cycle인 경우
        print("CYCLE")
        count+=len(que)
        break
      
      if visit[last-1]:             #  다음에 갈 곳이 방문할 곳인지 확인
        break
      
      """
      [1, 5], [5, 3], [3, 4], [4, 5], [5, 3], [3, 4], [4, 5]
      같은 경우 어떻게 3,4,5가 Cycle 이란 것을 확인할까
      
      
      """
      que.append([last,togo[last-1]])     # 일단 방문한 곳이 아니고, 현재 Cycle이 아니면 다 추가
      visit[last-1]=True
      
      
    while que:
      if que[0][0]!=que[-1][1]:
        que.popleft()

      if que[-1][1]==que[0][0]:     #  완벽히 cycle인 경우
        print("CYCLE")
        count+=len(que)
        break
      
    print(que)

  print("정답은 : ",n-count)
  
  