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
4. 큐가 빌 때까지 2번 반복. 모든 칸이 큐에 1번씩 들어가므로 시간복잡도 O(n)
"""


def bfs(visit,y,x):
  dx=[-1,1,0,0]
  dy=[0,0,1,-1]
  cnt=0
  temp=0
  
  visit[y][x]=True # 방문했는지 안했는지. 
  que=deque()     #que에는 방문한 곳 기준 주변에 1인 것들을 넣는다. 
  que.append([y,x])
  while que:
    cur=que.popleft()
    
    for i in range(4):
      nx=dx[i]+cur[1]
      ny=dy[i]+cur[0]
      
      if visit[ny][nx]:
        continue
      
      
      

    
    
  