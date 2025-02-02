from collections import deque
import sys

input=sys.stdin.readline
N=int(input())

zido=[]

for _ in range(N):
  zido.append(list(map(int,input().strip())))

visit=[[False]*N for _ in range(N)]

town=0

def BFS(y,x):
  global town
  town+=1
  
  que=deque()
  que.append([y,x])
  visit[y][x]=True
  
  width=0
  
  while que:
    cur=que.popleft()
    width+=1
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    for i in range(4):
      nx=cur[1]+dx[i]
      ny=cur[0]+dy[i]

      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue
      if visit[ny][nx]:
        continue
      if zido[ny][nx]==0:
        continue
      que.append([ny,nx])
      visit[ny][nx]=True
      
  return width
      
res=[]
for y in range(N):
  for x in range(N):
    if zido[y][x]==1 and visit[y][x]==False:
      res.append(BFS(y,x))

print(town)
res=sorted(res)
for i in res:
  print(i)
















