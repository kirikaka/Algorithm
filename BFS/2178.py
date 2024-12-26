from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())

path=[]
for _ in range(n):
  row=list(map(int,input()))
  path.append(row)


dist=[[0]*m for _ in range(n)]

def dfs(dist,y,x):
  dx=[-1,0,0,1]
  dy=[0,-1,1,0]
  que=deque()
  que.append([y,x])
  
  dist[y][x]=1
  while que:
    next=que.popleft()
    for i in range(4):
      ny=dy[i]+next[0]
      nx=dx[i]+next[1]
      if nx<0 or ny<0 or ny>=n or nx>=m:
        continue
      if path[ny][nx]==0:
        continue
      if dist[ny][nx]==0: #아직 방문안한, 거리가 0으로 표시된 지점을 방문
        que.append([ny,nx]) # 큐에 좌표 넣고
        dist[ny][nx]=dist[next[0]][next[1]]+1 #거리를 하나씩 올리기
    
dfs(dist,0,0)
print(dist[n-1][m-1])      
