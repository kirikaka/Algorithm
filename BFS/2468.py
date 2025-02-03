from collections import deque
import sys,copy

input=sys.stdin.readline

N=int(input())
rain=[]
cnt=0
for _ in range(N):
  tmp=list(map(int,input().split()))
  if cnt<max(tmp):
    cnt=max(tmp)
  rain.append(tmp)

res=[]

def BFS(y,x):
  que=deque()
  que.append([y,x])
  visit[y][x]=True
  
  while que:
    cur=que.popleft()
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    for i in range(4):
      nx=dx[i]+cur[1]
      ny=dy[i]+cur[0]
      
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      if sink[ny][nx]==0:
        continue
      if visit[ny][nx]:
        continue
      que.append([ny,nx])
      visit[ny][nx]=True

for i in range(cnt+1):
  sink=copy.deepcopy(rain)
  visit=[[False]*N for _ in range(N)]
  
  for y in range(N):
    for x in range(N):
      if sink[y][x]<=i:
        sink[y][x]=0
      else:
        sink[y][x]=1

  
  count=0
  for y in range(N):
    for x in range(N):
      if sink[y][x]==1 and visit[y][x]==False:
        
        BFS(y,x)
        count+=1
        
  res.append(count)


print(max(res))  
  
  

















