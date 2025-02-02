from collections import deque
import sys

input=sys.stdin.readline

M,N,K=map(int,input().split())

board=[[0]*N for i in range(M)]
visit=[[False]*N for i in range(M)]

for _ in range(K):
  x_left,y_left,x_right,y_right=map(int,input().split())
  
  for y in range(y_left,y_right):
    for x in range(x_left,x_right):
      board[y][x]=1
  
area=0  

def BFS(y,x):
  global area
  area+=1
  que=deque()
  
  que.append([y,x])
  visit[y][x]=True
  width=0
  
  while que:
    cur=que.popleft()
    width+=1
    
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    for i in range(4):
      ny=cur[0]+dy[i]
      nx=cur[1]+dx[i]
      
      if nx<0 or ny<0 or nx>=N or ny>=M:
        continue
      if visit[ny][nx]:
        continue
      if board[ny][nx] == 1:
        continue        
      que.append([ny,nx])
      visit[ny][nx]=True
      
  return width
      
      
res=[]
for y in range(M):
  for x in range(N):
    if board[y][x]==0 and visit[y][x]==False:
      res.append(BFS(y,x))
  
print(area)
res=sorted(res)
print(" ".join(map(str,res)))













