from collections import deque
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
miro=[list(map(int,input().strip())) for _ in range(n)]



"""
* 방문여부랑 비슷하게 거리를 표시하는 이차원 배열 만들기
1. 시작하는 칸을 큐에 넣고 방문 표시
2. 큐의 첫 원소 꺼내서 상하좌우 인접한 칸에 1이 있는지 진행
2-1. 그 과정에서 그림판보다 크거나 0이하면 continue
3. 방문했던 칸이면 continue(dist[ny][nx]), 
아니면 거기까지의 거리를 계산해서 넣기(이전 거리와 비교)
4. 큐가 빌대까지 반복.
5. 1,1에서 시작
"""

dist=[[0]*m for _ in range(n)]


def bfs(dist,y,x):
  que=deque()
  que.append([y,x])
  
  dx=[-1,1,0,0] #좌우상하
  dy=[0,0,1,-1]
  dist[y][x]=1
  
  while que:
    cur=que.popleft()
    cur_dist=dist[cur[0]][cur[1]]
    

    for i in range(4):
      nx=dx[i]+cur[1]
      ny=dy[i]+cur[0]
      
      if nx<0 or ny<0 or nx>=m or ny>=n:
        continue
      if miro[ny][nx]==0:
        continue
      
      if dist[ny][nx] == 0:
        dist[ny][nx]=cur_dist+1
        que.append([ny,nx])
        
bfs(dist,0,0)

print(dist[n-1][m-1])
      
      
      
