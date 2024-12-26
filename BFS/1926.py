from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())

pic=[]
for _ in range(n):
  row=list(map(int,sys.stdin.readline().split()))
  pic.append(row)

visited=[[False]*m for _ in range(n)]


def bfs(visited,y,x):
  temp=0
  dx=[-1,0,0,1] #열 좌상하우
  dy=[0,1,-1,0] #행 좌상하우
  
  visited[y][x]=True
  que=deque()
  que.append([y,x])
  while que:
    value=que.popleft()
    temp+=1
    for i in range(4):
      ny=dy[i]+value[0]
      nx=dx[i]+value[1]
      if nx<0 or nx>=m or ny<0 or ny>=n: #좌표가 벗어나면
        continue
      if pic[ny][nx]==0:
        continue
      if not visited[ny][nx]: #방문안한 그림을 방문하면
        visited[ny][nx]=True #해당 그림을 방문으로 바꾸고
        que.append([ny,nx]) # 큐에 넣는다. 
    
  return temp
        
res=[]
for i in range (n):
  for j in range(m):
    if pic[i][j]==1 and visited[i][j]==False: #그림이며 방문한적이 없을 때 bfs 시작
      res.append(bfs(visited,i,j))


print(len(res))
if len(res)==0:
  print(0)
else:
  print(max(res))