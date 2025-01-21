import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
paint=[list(map(int,input().split())) for _ in range(n)]

visit=[[False]*m for _ in range(n)]

"""
1. 시작하는 칸을 큐에 넣고 방문했다는 표시 남김
2. 큐에서 원소꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번 진행
3. 해당칸 이전 방문했으면 continue, 첫 방문이면 방문 표시 남기고 해당 칸을 큐 삽입
3-1. 그림판을 넘는지 안넘는지 확인.
3-2. 그림인지 아닌지 판단.
4. 큐가 빌 때까지 2번 반복. 모든 칸이 큐에 1번씩 들어가므로 시간복잡도 O(n)
"""
answer=[]

def bfs(visit,y,x):
  dx=[-1,1,0,0]
  dy=[0,0,1,-1]
  temp=0
  
  visit[y][x]=True # 방문했는지 안했는지. 
  que=deque()     #que에는 방문한 곳 기준 주변에 1인 것들을 넣는다. 
  que.append([y,x])
  while que:
    cur=que.popleft()
    temp+=1
    for i in range(4):
      nx=dx[i]+cur[1]   #dx,dy 순회하면서 주위의 방문안한 곳이나 그림있는곳이 있는지 확인
      ny=dy[i]+cur[0]
      if nx<0 or ny<0 or nx>=m or ny>=n: #그림판 넘는지 안넘는지 확인.
        continue
      if paint[ny][nx]==0:  
        continue
      
      
      if not visit[ny][nx]:
        visit[ny][nx]=True
        que.append([ny,nx])
        
  return temp
        
      
for i in range(n):
  for j in range(m):
    if paint[i][j]==1 and visit[i][j]==False:
      answer.append(bfs(visit,i,j))      

    
print(len(answer))
print(max(answer))
  